import os
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import random
import cohere
from study_plan_generator.cohere_api import generate_study_plan

# Initialize FastAPI app
app = FastAPI()

# Initialize Cohere client
cohere_client = cohere.Client('aByFTDxbymTL0XLjwVmpDAXwoVvILhl27MyppZQM')  # Replace with your actual Cohere API key

# Define the file path for questions
QUESTIONS_FILE_PATH = os.path.join(os.path.dirname(__file__), 'questions.json')

def get_random_questions():
    # Load and shuffle questions from the JSON file
    with open(QUESTIONS_FILE_PATH) as f:
        questions = json.load(f)
        random.shuffle(questions)  # Shuffle the questions
        return questions[:30]

# Define the root route
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Endpoint to serve quiz questions
@app.get("/quiz")
def get_quiz():
    return {"questions": get_random_questions()}

# Define the Pydantic model for incoming user answers
class UserAnswer(BaseModel):
    id: int
    answer: int

@app.post("/check_answers")
def check_answers(user_answers: List[UserAnswer]):
    # Load questions from the JSON file
    with open(QUESTIONS_FILE_PATH) as f:
        questions = json.load(f)
    
    # Store the incorrect answers
    incorrect_answers = []
    for user_answer in user_answers:
        question = next(q for q in questions if q["id"] == user_answer.id)
        if question["correctAnswer"] != user_answer.answer:
            incorrect_answers.append(question)
    
    # Generate a study plan using Cohere for incorrect answers
    if incorrect_answers:
        try:
            # Extract topics of the incorrect answers and use a set to ensure uniqueness
            incorrect_topics = set(q["topic"] for q in incorrect_answers)  # Using set here

            study_plans = []
            # Generate a separate study plan for each topic in the set
            for topic in incorrect_topics:
                study_plan = generate_study_plan(topic)  # Generate the study plan for each topic
                study_plans.append({topic: study_plan})  # Add the plan for the specific topic
            
            return {"incorrect_answers": incorrect_answers, "study_plans": study_plans}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error generating study plan: {e}")
    
    return {"incorrect_answers": [], "study_plans": "No incorrect answers, no study plan needed."}


