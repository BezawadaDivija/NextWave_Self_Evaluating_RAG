from retriever import retrieve_information
from evaluator import evaluate_lesson
from datetime import datetime

question = "What is RAG?"

trusted_data = retrieve_information(question)
trusted_context = "\n\n".join(trusted_data)

wrong_lesson = """
RAG is a type of smartphone made by Apple.
It does not retrieve any external information.
RAG guarantees that every AI answer is always correct.
"""

print("Testing evaluator with an incorrect lesson...")

result = evaluate_lesson(wrong_lesson, trusted_context)

print("\nEVALUATION RESULT:")
print(result)

if "STATUS: REJECTED" in result:

    with open("rejection_log.txt", "a", encoding="utf-8") as file:
        file.write("\n" + "=" * 50 + "\n")
        file.write("Date: " + str(datetime.now()) + "\n")
        file.write("Question: " + question + "\n")
        file.write("Rejected Lesson:\n" + wrong_lesson + "\n")
        file.write("Evaluator Feedback:\n" + result + "\n")

    print("\nRejection saved successfully!")

else:
    print("\nLesson was not rejected. No rejection log saved.")