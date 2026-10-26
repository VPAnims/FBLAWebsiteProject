**Naming:**

| Thing: | Style: | Example: |
| :---- | :---- | :---- |
| Files and folders | kebab-case | report-issue.html |
| CSS classes and ids | kebab-case | .trail-card, \#issue-form |
| JS variables and functions | camelCase | trailName, loadTrails() |
| Python variables and functions | snake_case | show_home_page |
| JS constants | UPPER\_SNAKE\_CASE | MAX\_VOLUNTEERS |
| Database tables and columns | snake\_case | trails, trail\_id |

Rules:

1. Names say what the thing is.  
2. Functions start with a verb (get, load, show, save).  
3. True/false variables start with is or has (isOpen, hasPhoto).

**Comments:**

| Where: | What to write: | Example: |
| :---- | :---- | :---- |
| Top of every file | What the file does | // Handles the equipment page |
| Above every function (unless purpose already clear from the name) | What it does in one line | // Loads all trails and shows them on the page |
| Inside code | Only when the reason isn’t obvious | // Skip completed issues so the map only shows open work |

Rules:

1. Explain why, not what. The code already shows what.  
2. Use full sentences with correct spelling.  
3. Delete old code instead of commenting it out.

**Formatting:**

| Rule: | Setting: |
| :---- | :---- |
| Indentation | 2 spaces in HTML, CSS, and JS; 4 spaces in Python (Python standard). |
| Quotes in JS | Single (‘hello’) |
| Quotes in HTML | Double (class=”trail-card”) |
| Semicolons in JS | Always |
| Blank lines | One between functions and CSS blocks |

Rules:
 
2. Never push code that hasn't been formatted.

**Documentation:**

| File: | What goes in it: |
| :---- | :---- |
| README.md | What TrailTrack is, how to run it, who made it |
| docs/obstacle-log.md | Problems we ran into and how we fixed them |
| docs/sources.md | Every image, library, and fact we used, with a link |

Rules:

1. Keep the README.md up to date.  
2. Keep the obstacle-log.md up to date.  
3. Keep the sources.md up to date.

Obstacle log entry format:

Date:  
Problem:  
What we tried:  
How we fixed it:

**Error handling:**

| Where: | What to do: |
| :---- | :---- |
| Forms | Check inputs before submitting and show a clear message next to the field |
| Loading data | Wrap it in try/catch and show a friendly message if it fails |
| Server | Check every request, even if the form already did |
| Browser console | No red errors on any page before pushing |
