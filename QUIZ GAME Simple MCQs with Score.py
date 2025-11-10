# QUIZ GAME - Simple MCQs with Score Counter

# Step 1: Create a list of questions, options, and correct answers
questions = [
    "1. What is the capital of France?",
    "2. Which programming language is this quiz written in?",
    "3. What does CPU stand for?",
    "4. Who developed Python?",
]

options = [
    ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
    ["A. Java", "B. Python", "C. C++", "D. HTML"],
    ["A. Central Processing Unit", "B. Central Programming Unit", "C. Control Processing Unit", "D. Computer Power Unit"],
    ["A. Dennis Ritchie", "B. Guido van Rossum", "C. James Gosling", "D. Elon Musk"],
]

answers = ["C", "B", "A", "B"]  # Correct options

# Step 2: Initialize score
score = 0

# Step 3: Ask questions one by one
for i in range(len(questions)):
    print("\n" + questions[i])  # Print the question
    for option in options[i]:    # Print all options
        print(option)
    
    user_answer = input("Enter your answer (A/B/C/D): ").upper()  # Take user input
    
    # Step 4: Check if answer is correct
    if user_answer == answers[i]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong! The correct answer is:", answers[i])

# Step 5: Show final score
print("\n🎉 Quiz Completed!")
print("Your total score is:", score, "/", len(questions))
