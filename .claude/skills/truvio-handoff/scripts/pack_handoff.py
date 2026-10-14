#!/usr/bin/env python3
"""Pack a Truvio task folder into a handoff zip and check it before it ships.

usage: pack_handoff.py <task-folder> [--md handoff-x.md] [--out path.zip] [--exclude GLOB ...]

- Finds the handoff markdown (handoff-*.md in the folder) unless --md names it.
- Zips the folder under one top-level directory named after it, so links in the
  markdown work the same in the repo and in the unzipped copy.
- Fails on: a markdown link or image that points at a missing file, a licensed
  Museo Slab font file, a likely secret (.env, keys, credentials).
- Warns on: backticked file paths outside the zip, font files without a licence
  next to them, file names with secret/token/password, a zip over 25 MB
  (the usual email attachment cap).
"""
import argparse, fnmatch, os, re, sys, zipfile

SKIP = [".git", ".DS_Store", "Thumbs.db", "__pycache__", "*.pyc", "~$*", "*-workspace", "*.zip", ".~lock*"]
SECRET_NAMES = [".env", ".env.*", "*.pem", "*.key", "*.p12", "id_rsa*", "credentials*"]
MAYBE_SECRET = ["*secret*", "*token*", "*password*"]   # warn only: design-tokens.json is normal
SECRET_TEXT = re.compile(r"(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{12,}|\bsk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}", re.I)
TEXT_EXT = {".md", ".txt", ".html", ".css", ".js", ".json", ".py", ".sh", ".svg", ".csv", ".yml", ".yaml"}
FONT_EXT = {".otf", ".ttf", ".woff", ".woff2"}
MB = 1024 * 1024


def skipped(name, extra):
    return any(fnmatch.fnmatch(name, p) for p in SKIP + extra)


def collect(root, extra):
    files = []
    for d, dirs, names in os.walk(root):
        dirs[:] = sorted(x for x in dirs if not skipped(x, extra))
        for n in sorted(names):
            if not skipped(n, extra):
                files.append(os.path.relpath(os.path.join(d, n), root))
    return files


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--md")
    ap.add_argument("--out")
    ap.add_argument("--exclude", nargs="*", default=[])
    a = ap.parse_args()

    root = os.path.abspath(a.folder.rstrip("/"))
    name = os.path.basename(root)
    if not os.path.isdir(root):
        sys.exit(f"not a folder: {root}")

    mds = [a.md] if a.md else sorted(f for f in os.listdir(root) if fnmatch.fnmatch(f, "handoff*.md"))
    if len(mds) != 1:
        sys.exit(f"expected one handoff*.md in {root}, found {mds or 'none'}. Name it with --md.")
    md_rel = mds[0]
    md_text = open(os.path.join(root, md_rel), encoding="utf-8").read()

    files = collect(root, a.exclude)
    have = set(files)
    errors, warns = [], []

    # Links and images in the markdown must resolve inside the zip.
    for target in re.findall(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", md_text):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        p = os.path.normpath(target.split("#")[0])
        if p not in have:
            errors.append(f"markdown links to a file that isn't in the zip: {target}")

    # Backticked paths are softer: they may be repo paths or commands.
    for tok in sorted(set(re.findall(r"`([^`\s]+\.[A-Za-z0-9]{1,5})`", md_text))):
        p = os.path.normpath(tok)
        if p not in have and not os.path.exists(os.path.join(root, p)):
            warns.append(f"backticked path not in the zip (fine for a repo path): {tok}")

    total = 0
    for f in files:
        full = os.path.join(root, f)
        base, ext = os.path.basename(f), os.path.splitext(f)[1].lower()
        total += os.path.getsize(full)
        if ext in FONT_EXT:
            if "museo" in base.lower():
                errors.append(f"licensed font in the zip, remove it: {f}")
            elif not any("licen" in x.lower() for x in os.listdir(os.path.dirname(full))):
                warns.append(f"font without a licence file next to it: {f}")
        if any(fnmatch.fnmatch(base.lower(), p) for p in SECRET_NAMES):
            errors.append(f"looks like a secret, keep it out of the zip: {f}")
        elif any(fnmatch.fnmatch(base.lower(), p) for p in MAYBE_SECRET):
            warns.append(f"check this file holds no secret: {f}")
        elif ext in TEXT_EXT and os.path.getsize(full) < 2 * MB:
            if SECRET_TEXT.search(open(full, encoding="utf-8", errors="ignore").read()):
                errors.append(f"text that looks like a key or token: {f}")

    out = os.path.abspath(a.out or os.path.join(root, f"{name}-handoff.zip"))
    if errors:
        print("NOT PACKED")
        for e in errors:
            print("  error:", e)
        for w in warns:
            print("  warning:", w)
        sys.exit(1)

    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for f in files:
            z.write(os.path.join(root, f), os.path.join(name, f))
    with zipfile.ZipFile(out) as z:
        bad = z.testzip()
        listed = z.namelist()
    if bad:
        sys.exit(f"zip test failed on {bad}")

    size = os.path.getsize(out)
    print(f"packed: {out}")
    print(f"handoff: {name}/{md_rel}")
    print(f"files: {len(listed)}, {total / MB:.2f} MB unpacked, {size / MB:.2f} MB zipped, zip test OK")
    for f in listed:
        print("  ", f)
    if size > 25 * MB:
        warns.append(f"zip is {size / MB:.1f} MB, over the 25 MB email cap. Share a link or split it.")
    for w in warns:
        print("warning:", w)


if __name__ == "__main__":
    main()
