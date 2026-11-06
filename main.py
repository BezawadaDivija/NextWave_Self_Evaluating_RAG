import os
from dotenv import load_dotenv
from google import genai

from retriever import retrieve_information
from generator import generate_lesson
from evaluator import evaluate_lesson

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def correct_lesson(old_lesson, trusted_context, feedback):

    prompt = f"""
You are an expert lesson corrector.

Rewrite the rejected lesson using ONLY the trusted information.

TRUSTED INFORMATION:
{trusted_context}

REJECTED LESSON:
{old_lesson}

EVALUATOR FEEDBACK:
{feedback}

INSTRUCTIONS:
1. Correct all identified mistakes.
2. Use very simple English.
3. Use short sentences.
4. Do not add unsupported facts.
5. Keep the lesson suitable for a beginner.

Return only the corrected lesson.
"""

    print("\nCorrecting the rejected lesson...")

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text


def run_pipeline():

    question = "What is RAG?"

    print("\nSTUDENT QUESTION:")
    print(question)

    print("\nRetrieving trusted information...")

    retrieved_data = retrieve_information(question)

    if not retrieved_data:
        print("No trusted information found.")
        return

    trusted_context = "\n\n".join(retrieved_data)

    print("\nGenerating initial lesson...")

    # Intentionally wrong lesson for testing
    lesson = generate_lesson(question)

    max_attempts = 3

    for attempt in range(1, max_attempts + 1):

        print(f"\nEVALUATION ATTEMPT: {attempt}")

        evaluation = evaluate_lesson(
            lesson,
            trusted_context
        )

        print("\nEVALUATION RESULT:")
        print(evaluation)

        if "STATUS: APPROVED" in evaluation.upper():

            print("\nLESSON APPROVED!")

            with open(
                "approved_lesson.txt",
                "w",
                encoding="utf-8"
            ) as file:
                file.write(lesson)

            print("Final lesson saved successfully!")
            return

        print("\nLESSON REJECTED!")

        with open(
            "rejection_log.txt",
            "a",
            encoding="utf-8"
        ) as file:
            file.write("\n" + "=" * 50 + "\n")
            file.write(f"Attempt: {attempt}\n")
            file.write("Rejected Lesson:\n")
            file.write(lesson + "\n")
            file.write("Evaluator Feedback:\n")
            file.write(evaluation + "\n")

        if attempt < max_attempts:

            lesson = correct_lesson(
                lesson,
                trusted_context,
                evaluation
            )

        else:
            print("\nMaximum attempts reached.")
            print("Lesson could not be approved.")


if __name__ == "__main__":

    try:
        run_pipeline()
    finally:
        client.close()