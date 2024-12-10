import cohere

# Initialize Cohere client
co = cohere.Client('nbNa6GMc481fF7TvclqStOTLwOZGef9pcwnaYD1m')  # Replace with your actual API key

def generate_study_plan(topic):
    """
    Generate a 4-week study plan for a specific topic in data science.
    """
    prompt = f"""
    I am learning about {topic}. Create a detailed 4-week study plan to help me master it. The study plan should cover the basics of the topic, provide a structured weekly breakdown, recommend books, courses, and tutorials, and include practical exercises for hands-on experience. The plan should also provide a clear set of objectives for each week, list specific topics to cover, and offer project suggestions for real-world application. Make sure the study plan is well-structured, starting from fundamentals to more advanced concepts.
    For example, if the topic is Neural Networks:
    - **Week 1**: Foundations of Neural Networks (cover perceptrons, activation functions, backpropagation)
    - **Week 2**: Training Neural Networks (cover optimization, gradient descent, regularization techniques)
    - **Week 3**: Deep Neural Networks (DNNs), CNNs, RNNs (cover transfer learning and advanced architectures)
    - **Week 4**: Advanced Applications (cover GANs, Reinforcement Learning, and real-world applications like NLP or computer vision)
    Include resources like books, online courses, tutorials, and practical projects to apply the learned concepts.
Each topic should have its own plan without combining them, and the study plan should be tailored to each topic individually within 500 or 600 words.
    """
    response = co.generate(
        model='command-xlarge-nightly',  # Use Cohere's recommended text generation model
        prompt=prompt,
        max_tokens=999,
        temperature=0.7,  # Controls creativity (0.7 is a balanced choice)
        k=0,
        stop_sequences=[]
    )
    
    return response.generations[0].text.strip()

