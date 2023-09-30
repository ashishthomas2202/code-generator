import os
import openai
import ast


def analyze(project):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    output_format = {
        "questions": ["question 1", "question 2", "question 3"]
    }
    # Updated prompt with more specific instructions
    # prompt = f"Translate the user requirements: {requirements}, and generate additional business related questions required for software development based on these requirements.Note: The questions should be formatted as a Python dictionary with attributes and key value pair in double quotes like {output_format}"
    prompt = f"As a software development firm, we aim to better understand your requirements for the project related to {project}. Please provide us with additional insights and details that will help us tailor our approach to meet your business needs. We will frame our questions in a way that is easy to understand for non-technical clients.  Please generate 10 questions. if its a technical question, please provide some recommended one word answers. here is the output format for the questions: {output_format}."
    response = createResponse(prompt)

    questions = ast.literal_eval(response)['questions']

    # print("parsed questions", questions)

    detailed_requirements = []

    for question in questions:

        done = False
        while not done:
            answer = input(f"{question}: ")
            if len(answer) > 0:
                detailed_requirements.append({
                    "question": question,
                    "answer": answer
                })
                done = True

    # project["detailed_requirements"] = detailed_requirements

    return detailed_requirements


def createResponse(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,  # Adjust temperature for desired creativity
        max_tokens=2800,    # Adjust max_tokens based on desired response length
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response.choices[0].text
