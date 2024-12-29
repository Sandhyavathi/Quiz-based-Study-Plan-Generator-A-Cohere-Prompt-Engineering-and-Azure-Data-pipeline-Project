import streamlit as st
import requests
import json

# API URLs
QUIZ_API_URL = "http://20.235.161.127/quiz"  # Replace with your FastAPI quiz endpoint
CHECK_ANSWERS_API_URL = "http://20.235.161.127/check_answers"  # Replace with your FastAPI check answers endpoint

# Initialize session state for quiz data and answers
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = []
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}

# Title for the app
st.title("Interactive Quiz and Study Plan Generator")

# Fetch quiz questions if not already fetched
if not st.session_state.quiz_data:
    try:
        response = requests.get(QUIZ_API_URL)
        response.raise_for_status()
        st.session_state.quiz_data = response.json().get("questions", [])
    except Exception as e:
        st.error(f"Failed to load quiz questions: {e}")
        st.session_state.quiz_data = []

# Display quiz questions
st.header("Take the Quiz")
if st.session_state.quiz_data:
    for question in st.session_state.quiz_data:
        question_id = question["id"]
        st.subheader(f"Q: {question['question']}")
        selected_option = st.radio(
            "Choose your answer:",
            options=enumerate(question["options"], 1),
            format_func=lambda x: x[1],
            key=f"question_{question_id}",
            index=st.session_state.user_answers.get(question_id, -1) - 1
            if question_id in st.session_state.user_answers
            else 0,
        )
        # Save the answer in session state
        st.session_state.user_answers[question_id] = selected_option[0]

    # Submit answers and get results
    # Submit answers and get results
    if st.button("Submit Answers"):
        user_answers = [
            {"id": q_id, "answer": answer}
            for q_id, answer in st.session_state.user_answers.items()
        ]
        try:
            response = requests.post(
                CHECK_ANSWERS_API_URL,
                headers={"Content-Type": "application/json"},
                data=json.dumps(user_answers),
            )
            response.raise_for_status()
            results = response.json()

            # Display incorrect answers and study plans
            incorrect_answers = results.get("incorrect_answers", [])
            study_plans = results.get("study_plans", [])

            if incorrect_answers:
                st.header("Review Your Incorrect Answers")
                for question in incorrect_answers:
                    st.error(
                        f"Q{question['id']}: {question['question']}\n\n"
                        f"Correct Answer: {question['options'][question['correctAnswer'] - 1]}\n"
                        f"Topic: {question['topic']}"
                    )

                st.header("Generated Study Plans")
                for plan in study_plans:
                    for topic, study_plan in plan.items():
                        st.subheader(f"Study Plan for {topic}")
                        st.write(study_plan)
            else:
                st.success("Great job! All your answers are correct.")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to submit answers: {e}")


