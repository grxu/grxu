# Handoff template

Keep the section order. Drop a section only when it really has nothing in it, and keep "Where it stands", "Next steps" and "Open items" every time. The worked example is `truvio/pim-ads/three-steps/handoff-three-steps.md` in the grxu repo.

```markdown
# Handoff: <task name> (<product or campaign>)

<Date>. Work by Grady with Claude. Repo folder: `<path>` on branch `<branch>` (<repo>).
<On the Mac, swap the repo line for the OUTPUTS path.>

## Where it stands
- 3 to 5 bullets. What exists, what is final, what hasn't happened yet
  ("Nothing has been generated in Higgsfield yet"), what is blocking.

## Next steps
1. Numbered, in the order they happen. Start each one with who does it,
   whenever it isn't obvious. Name the file or tool for each step.

## Open items

| Item | Who | Why it matters |
|---|---|---|
| <missing input, unconfirmed fact, sign-off> | <a person or team the chat named, or "unknown, ask Grady"> | <what breaks or stays wrong without it> |

## Copy (final, from the brief)
<The brief exactly as given: on-design lines, ads headline and body, link, visual direction.
For non-ad work, swap this for "Brief" and quote the ask.>

## Decisions

Grady chose (<date>):
- <Decision>. <One line on what it changed.>

Claude's calls (not reviewed yet):
- <Call>. <Why, in one line.>

## What was made
<One line per image saying what it shows and which parts are stand-ins.>

![<alt>](<relative path>)

## Files

| File | What it is |
|---|---|
| `<relative path>` | <What it is, and whether it's final, a stand-in or source.> |

## How to edit
- <The quickest way to open it.>
- <The command to re-render or rebuild, with repo paths marked.>

## QA results
- <Checks that ran, with numbers: margins, colour samples, fonts, clearances.>

## Session log
- <Date>: <what happened>. Include what was tested and dropped, and commit ids.

## Related
- `<path>`: <how it relates: same campaign, the skill that made it, a reference file.>
```

## Notes per section

- **Where it stands.** Write it last. It's the summary of everything below it.
- **Next steps.** A teammate should be able to start on step 1 without asking anything. If step 1 is "wait for X", list X under open items and say who is chasing it.
- **Open items.** Every blocker, missing input and unconfirmed fact from the chat goes here, including the ones flagged in passing. Put the owners exactly as the chat named them. No guessing.
- **Decisions.** Each one carries its reason. "Three columns instead of a list" means nothing without "the badge is wide". Leave out options nobody tried. An option tested and dropped stays in, with the reason, so nobody tests it again.
- **What was made.** Mark stand-ins on the image line itself, so nobody mistakes a mock for the final.
- **Files.** List every file in the zip. Group a folder when its contents are obvious (`source/fonts/`).
- **QA.** Only checks that actually ran, with their numbers. Leave the section out when nothing was measured.
