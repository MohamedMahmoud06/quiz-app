from model import get_quiz_data
def start_quiz(questions):
    """
    Starts the quiz and keeps track of the score.
    """
    score = 0
    for idx, q in enumerate(questions):
        print(f"\nQuestion {idx + 1}: {q['question']}")
        for i, choice in enumerate(q["choices"]):
            print(f"{i + 1}. {choice}")
        
        try:
            user_answer = int(input("Your choice (1-4): "))
            if q["choices"][user_answer - 1] == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was: {q['answer']}")
        except (ValueError, IndexError):
            print("Invalid input! Moving to the next question.")
    
    print(f"\nQuiz finished! Your score: {score}/{len(questions)}")

def main():
    print("Welcome to the Quiz App!")
    quiz_data = get_quiz_data()

    # Category selection
    print("\nAvailable Categories:")
    for category in quiz_data.keys():
        print(f"- {category}")
    category = input("\nEnter a category: ").strip()
    while category not in quiz_data:
        category = input("Invalid category. Enter a valid category: ").strip()

    # Difficulty selection
    difficulty = input("\nSelect difficulty (easy, medium, hard): ").lower()
    while difficulty not in ["easy", "medium", "hard"]:
        difficulty = input("Invalid choice. Select difficulty (easy, medium, hard): ").lower()

    # Number of questions
    try:
        num_questions = int(input("\nEnter the number of questions: "))
    except ValueError:
        print("Invalid input! Defaulting to 5 questions.")
        num_questions = 5

    # Get the selected questions
    all_questions = quiz_data[category][difficulty]
    selected_questions = all_questions[:num_questions]

    # Start the quiz
    start_quiz(selected_questions)

if __name__ == "__main__":
    main()
