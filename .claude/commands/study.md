# LeetCode Pattern Study Session

Run a focused, pattern-based algorithm study session. Follow these steps exactly in order.

---

## Step 1 — Assess Current State

Read `progress.md` and scan all existing `patterns/*/\_pattern.md` files to understand:
- Which patterns have a `_pattern.md` (have been formally studied)
- Which are missing or have a "stub" / incomplete marker
- The most recently studied pattern (avoid repeating it back-to-back)

Also read `CLAUDE.md` for the current priority table.

---

## Step 2 — Select a Pattern

**If the user specified a pattern** (e.g., `/study two-pointers`), use that.

**Otherwise**, pick the highest-priority pattern from CLAUDE.md that either:
- Has no `_pattern.md` yet, OR
- Has a `_pattern.md` marked as `<!-- STATUS: stub -->` at the top

Tell the user: "Today's pattern: **[NAME]**. Reason: [1 sentence]."

---

## Step 3 — Teach the Pattern

Explain in exactly 3 parts — keep total under 300 words:

**The Concept** — What class of problem does this solve? What is the core intuition in one sentence?

**The Template** — The annotated Python skeleton. Every line that isn't obvious gets a comment. This is the thing to memorize.

**When to Recognize It** — 3-5 bullet signals in a problem description that indicate this pattern applies.

Example format:
```python
def pattern_template(arr):
    left = 0
    # initialize any window state here
    
    for right in range(len(arr)):
        # expand window: process arr[right]
        
        while <window_invalid_condition>:
            # shrink window: undo arr[left]
            left += 1
        
        # window is valid: update answer
    
    return answer
```

---

## Step 4 — Present a Problem

Pick ONE representative problem. Selection criteria:
- Medium difficulty
- High interview frequency (top 50 for this pattern)
- Demonstrates the core template, not a tricky variant

Present:
- Problem number, title
- The full problem statement (constraints + examples)
- LeetCode URL: `https://leetcode.com/problems/[slug]/`

---

## Step 5 — Guided Solve

1. Ask the user to **verbalize their approach** before writing any code. Wait for a response.
2. Confirm or redirect — if the approach is wrong, ask a leading question rather than just giving the answer.
3. Let the user write the solution. Guide through blockers with questions first, answers second.
4. Once it works: explain what makes this the "template" solution. What's the invariant being maintained? What's the time/space complexity?

---

## Step 6 — Write the Pattern File

Write or update `patterns/[pattern-name]/_pattern.md`:

```markdown
<!-- STATUS: complete -->
# [Pattern Name]

## The Concept
[1-2 sentence intuition]

## The Template
```python
# [fully annotated template code]
```

## When to Recognize It
- [signal 1]
- [signal 2]
- [signal 3]

## Problems Solved

| # | Title | Difficulty | Key Insight |
|---|-------|-----------|-------------|
| N | Title | Medium | [one sentence] |

## Gotchas / Failure Modes
- [when this pattern looks applicable but isn't]
- [common off-by-one or edge case]
```

If the file already exists, **add** the new problem to the table and update Gotchas if anything new was learned. Do not overwrite existing content.

---

## Step 7 — Update Progress Log

Append to `progress.md` (under `## Sessions`, most recent first):

```
- [YYYY-MM-DD] — [Pattern]: [Problem Title] (#N) — [one-sentence takeaway]
```

Also update the Status column in CLAUDE.md's pattern priority table if this pattern is now "complete" (has 2+ problems solved).

---

## Step 8 — Wrap Up

Tell the user two things:
1. **The one thing to remember** about today's pattern (the core invariant or "aha moment")
2. **What to do next session** (which pattern and why, based on priority)

Keep this to 3-4 lines max.
