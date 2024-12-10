# Quiz-Based Study Plan Generator

An **adaptive learning system** using **Generative AI**, designed for graduate and postgraduate students. This application generates personalized study plans based on quiz performance, helping students improve in areas where they struggle.

---

## Features

### Frontend
- **Streamlit**: A user-friendly interface for taking quizzes and viewing results.

### Backend
- **FastAPI**: Provides APIs for quiz handling and evaluation.
- **Cohere API**: Generates personalized 4- or 6-week study plans based on quiz performance.
- **MongoDB**: Stores user responses and performance data.

### Deployment
- **Docker**: Containerized backend for easy deployment.
- **Kubernetes (AKS)**: Orchestrates backend containers for scalability.
- **Azure Services**: Ensures cloud hosting and load balancing.

---

## Project Overview

### Objectives
- Develop a **Generative AI-driven system** to customize study plans for data science topics.
- Use **quizzes** to identify weak areas and tailor resources for improvement.
- Enable adaptive learning, focusing on individual student needs.

### Methodology
1. **Quiz Management**:
   - JSON-based database with 100 questions on data science.
   - Each session randomly selects 30 questions.
2. **Answer Evaluation**:
   - Submissions handled via REST APIs.
   - Responses evaluated to identify weak topics.
3. **Study Plan Generation**:
   - Cohere’s AI generates structured weekly objectives, resources, and practical exercises.
4. **Deployment**:
   - Containerized with Docker and deployed on Kubernetes for scalability.

### Outcomes
- Personalized learning experience with detailed study plans.
- Scalable, robust system leveraging cloud and AI technologies.
- Interactive interface for quizzes and study plans.

---

## Prerequisites

### Tools and Services
- Python 3.7+
- Docker
- Kubernetes CLI (`kubectl`)
- Azure CLI

### Libraries and Dependencies
Listed in `requirements.txt`.

---

## Installation and Setup

### Backend
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
