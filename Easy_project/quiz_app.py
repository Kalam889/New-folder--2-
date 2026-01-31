#QUIZ APP
user_name = input("Enter your name: ").strip().capitalize()
score_board = []
quiz = {
    "What is the capital of India?": "delhi",
    "Which city is known as the pink city?": "jaipur",
    "What is the capital of Maharashtra?": "mumbai",
    "What is the capital of West Bengal?": "kolkata"
}

for question, answer in quiz.items():
    user_ans = input(question + " ")
    if user_ans.lower() == answer.lower():
        score_board.append(1)
        print("Correct answer!")
    else:
        print("Wrong answer.")

Total = sum(score_board)  
No_of_keys = len(quiz)

print("Do you want to see the scorecard?")
user_input = input("yes/no: ").lower()

if user_input == "yes":
    print("Your total score is:", Total)
    print(f"{user_name} You got {Total} out of {No_of_keys}")
    percentage = (Total / No_of_keys) * 100
    print(f"Your score percentage is: {percentage:.2f}%")
    if percentage <= 50.00 :
        print("Need improvement")
    elif percentage > 50.00 and percentage <= 80 :
        print("Good ")
    else:
        print("Excellent")
else:
    print("Thank you for playing!")
