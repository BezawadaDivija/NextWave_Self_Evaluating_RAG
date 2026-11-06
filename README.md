Self-Evaluating RAG Learning System

1. Project Overview

This project is a Self-Evaluating Retrieval-Augmented Generation (RAG) system.

It helps beginner students learn Artificial Intelligence concepts using simple English.

The system retrieves trusted information, generates a lesson using Gemini AI, evaluates the lesson, and corrects mistakes when necessary.

2. Problem Statement

AI-generated answers can sometimes contain incorrect or unsupported information.

Beginners may find it difficult to identify these mistakes.

This project addresses that problem by checking generated lessons against a trusted knowledge base before approving them.

3. Project Objectives

- Retrieve trusted information from a knowledge base.
- Generate beginner-friendly lessons using Gemini AI.
- Evaluate generated lessons for accuracy, trust, and simplicity.
- Reject lessons containing mistakes.
- Correct rejected lessons using evaluator feedback.
- Save approved lessons and rejection logs.

 4. Technologies Used

- Python
- Google Gemini API
- ChromaDB
- Retrieval-Augmented Generation (RAG)
- Python dotenv

 5. System Workflow

1. Student enters a question.
2. Retriever searches the trusted knowledge base.
3. Gemini generates a simple lesson.
4. Evaluator checks the generated lesson.
5. If rejected, the system records mistakes and feedback.
6. Gemini corrects the rejected lesson.
7. The evaluator checks the corrected lesson again.
8. The approved lesson is saved.

 6. Evaluation Criteria

The evaluator checks three important areas:

- Accuracy: Is the lesson correct?
- Trust: Is the lesson supported by trusted information?
- Simplicity: Is the lesson easy for beginners to understand?

A lesson is approved only when all three checks pass.

7. Project Files

- retriever.py – Retrieves trusted information from ChromaDB.
- generator.py – Generates lessons using Gemini.
- evaluator.py – Evaluates generated lessons.
- main.py – Controls the complete workflow.
- test_evaluator.py – Tests the evaluator with an incorrect lesson.
- knowledge_base/ – Contains trusted learning information.
- approved_lesson.txt – Stores the final approved lesson.
- rejection_log.txt – Stores rejected lessons and evaluator feedback.

 8. How to Run the Project

Step 1: Install dependencies

bash
pip install -r requirements.txt


 Step 2: Configure Gemini API

Create a .env file in the project folder and add:

text
GEMINI_API_KEY=your_api_key_here


Do not share your API key publicly.
Step 3: Run the project

bash
python main.py


9. Expected Output

The system generates a beginner-friendly lesson and evaluates it.

If a lesson is rejected, the system corrects it and evaluates it again.

Approved lessons are saved in approved_lesson.txt.

Rejected lessons and evaluator feedback are saved in rejection_log.txt.

 10. Conclusion

This project demonstrates how Retrieval-Augmented Generation and AI-based evaluation can work together to generate more reliable learning content for beginners.