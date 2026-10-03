# Grade Reporter & Bug Hunt

This repository contains my Week 3 assignments exploring loops, conditional logic, and debugging strategies in Python.

## File Descriptions
* **grade_reporter.py**: A script that loops through a list of student scores, assigns letter grades, counts passes/fails, and calculates the class average.
* **bug_hunt.py**: A corrected script containing a while-loop that accurately calculates the sum of numbers from 1 to 5.

## Bug Hunt Reflection
The hardest bug to find was the logic error in the loop condition (`while count < 5`). Because it did not generate a red crash error message in the console, the code executed successfully but silently calculated the wrong mathematical total (10 instead of 15). I knew something was wrong because the final printed answer did not match our expected human calculation for adding 1, 2, 3, 4, and 5 together, which led me to realize the loop was stopping short and skipping the number 5 entirely.
