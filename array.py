# Program to calculate sum and average of scores

scores = []

n = int(input("Enter the number of scores: "))

for i in range(n):
  score = float(input(f"Enter score {i + 1}: "))
  scores.append(score)

# Calculate sum
total = sum(scores)
average = total / n if n > 0 else 0

print("Scores:", scores)
print("Sum of scores:", total)
print("Average of scores:", average)
