count = 1
total = 0

# BUG: Missing a colon at the end of the line causing a SyntaxError. 
# BUG: The loop condition was 'count < 5', which skipped the number 5 and gave a total of 10 instead of 15. Changed to '<= 5'.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Cannot concatenate a string with an integer directly (TypeError). Fixed using an f-string or converting total to str().
print(f"Sum of 1 to 5 is: {total}")
