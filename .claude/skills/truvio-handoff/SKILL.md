---
name: truvio-handoff
description: Pack a finished or paused Truvio task into a handoff. That means one markdown file saying where the work stands, what was decided and by whom, what is still open and what to do next, plus a .zip of the task folder (renders, mocks, prompt files, source, fonts with licences). A teammate, Grady next week, or a new Claude session can pick it up without the chat. Use it whenever Grady says handoff, hand off, wrap up, package this, compile what we did, zip the assets, pass it to the team, or is about to leave a task half done. It covers any Truvio work, from ads, Higgsfield prompts and mocks to decks, motion, booth artwork and website imagery, including when he never says "handoff". Not for making the deliverable itself (use the task's own skill, such as truvio-higgsfield-ad), and not for a status email.
---

# Truvio handoff

A handoff is for someone who wasn't in the chat. That could be a teammate, Grady after a week on other work, or a new Claude session in a fresh container. The chat disappears. The folder and the handoff stay. So the handoff has to stand on its own: the reader should be able to start on the next step without asking anything.

## Before anything

- Load the `truvio-work` skill. It carries the voice rules, the accuracy rules (never invent a number, date or owner) and the credit rules (what Grady did and didn't make). On the Mac, the same rules live in `~/Documents/Truvio CoWork/ABOUT ME/`.
- Find the task folder. In a cloud session it's `truvio/<campaign>/<task>/` in the grxu repo. On the Mac it's `OUTPUTS/<campaign>/<task>/`. If the work spans several folders, or has no folder yet, ask.

## 1. Gather

Work through these sources in order:
- **The conversation.** The brief word for word, each question asked and its answer, each change of direction, anything tested and dropped (and why).
- **The task folder.** Every file: what it is, what made it, and whether it's final, a stand-in or source.
- **Git history for the folder.** `git log --format='%h %ad %s' --date=short -- <folder>` gives dates and commit ids for the session log.
- **Existing files in the folder**, such as prompt files or specs. The handoff points to them. It doesn't copy them out.

Then sort every decision into two lists: **Grady chose** and **Claude's calls (not reviewed yet)**. A reader treats anything under "Decisions" as settled. An unreviewed call written as a decision quietly becomes final, and nobody ever looks at it again.

## 2. Ask only for the gaps

Ask in one AskUserQuestion call, with the most likely answer first. Typical gaps:
- who owns an open item
- a date
- whether a file is final
- who the reader is, when the request doesn't say (the default is anyone picking it up)

Skip anything the chat already answers. Never fill a gap with a guess. If Grady doesn't know either, write "unknown, ask Grady" in the open items table.

## 3. Write the handoff

Write `handoff-<task>.md` in the root of the task folder, following `references/handoff-template.md`. Read the template first. It holds the section order and what goes in each section.

- **Order.** Status, next steps, open items, the brief, decisions, what was made, files, how to edit, QA, session log, related. The reader's first questions are "where is it", "what do I do" and "what's blocking". History comes last.
- **Images.** Embed the key renders with relative links (`![Layout mock](mock-1x1.png)`), so they show in GitHub, VS Code and the unzipped folder. Truvio documents carry real visuals, not just text.
- **Paths.** Files in the zip get paths relative to the task folder. Repo paths, such as skills and scripts, go in backticks and are labelled as repo paths.
- **Credit.** Write "Work by Grady with Claude". Never write Grady as the author of something he didn't make (truvio-work section 2). Never give Claude credit for Grady's calls.
- **Stand-ins.** Name every stand-in (Arvo for Museo Slab, a reconstructed lockup, grey-bar UI, a black badge box) and what replaces it.
- **Copy.** Quote the brief exactly as given. Fix nothing.
- **Voice.** Follow truvio-work section 7. Then grep the file for semicolons, em dashes and the banned words. That's quicker and more reliable than rereading.

## 4. Pack the zip

```bash
python3 <this-skill>/scripts/pack_handoff.py <task-folder> [--exclude "*.mov" ...]
```

It writes `<task>-handoff.zip` in the task folder. Everything sits under one top-level folder, so the markdown's relative links work the same in the repo and in the unzipped copy. Earlier zips, `.git`, `.DS_Store` and scratch files are skipped.

**Errors stop it.** Fix them and run it again:
- A markdown link or image points at a file that isn't in the zip.
- A Museo Slab font file is in the folder. It's licensed, so it can't travel.
- A file looks like a secret (.env, keys, credentials, or text that looks like a token).

**Warnings need a judgement call:**
- A backticked path isn't in the zip. That's fine for a repo path.
- A font has no licence file next to it.
- A file name contains secret, token or password.
- The zip is over 25 MB, the usual email cap.

**What goes in:** everything the next person needs from the task folder. That means final renders, mocks, prompt files, source HTML, open-licence fonts with their licences, and the kit lockup.

**What stays out:** licensed fonts, anything holding a key or token, scratch files, and big intermediates (use `--exclude`).

A file from outside the folder goes in only when the handoff depends on it, such as a reference screenshot. Copy it into the folder and say where it came from.

## 5. Check

- Unzip into the scratchpad and Read one embedded image from the unzipped copy. The script already checks that every link resolves, and this confirms the files open.
- Read the handoff once as its reader. Could they do the first next step without asking anything? If not, fix whatever is missing.

## 6. Deliver

- **Cloud session:** commit the handoff and the zip, then push to the session branch. The container is wiped after the session. Ask before committing a zip over 25 MB.
- **Send the files.** Use SendUserFile for the zip (display attach) and the handoff (display render).
- **Keep the reply short.** Say where the work stands in one line. Give the number of open items and who holds them, the zip's file count and size, and anything left out and why.

## Reader variants

- **Anyone picking it up (default).** Use the full template.
- **Stakeholder** (Jess, the digital team). Keep status, decisions, open items and visuals. Drop the files table, commands, QA and session log. Zip only the finals.
- **A new Claude session.** Use the full template. In "How to edit", lead with the commands and the rules to keep.

## Several tasks in one session

Write one handoff per task folder. If a session touched several folders, write one for each and list them in the reply.
