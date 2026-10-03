# Start with the exact list provided
scores = [72, 45, 90, 61, 38]

# Initialize trackers for passing, failing, and total sum
passed_count = 0
failed_count = 0
total_sum = 0

# 1. Use a for loop to go through every score
for score in scores:
    total_sum += score  # Add up the scores for the average calculation later
    
    # 2. Use if / elif / else to work out the grade
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
        
    # 3. Print each score with its grade on its own line
    print(f"Score: {score} -> Grade: {grade}")
    
    # 4. Count how many learners passed (50 or more) or failed
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

# Calculate the average score
average = total_sum / len(scores)

# Print final required metrics
print("\n--- Summary Statistics ---")
print(f"Learners Passed: {passed_count}")
print(f"Learners Failed: {failed_count}")
print(f"Average Score: {round(average, 1)}")
