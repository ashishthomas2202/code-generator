import os
import ast
import openai


def analyze(requirements):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    output_format = {
        "questions": ["question 1", "question 2", "question 3"]
    }
    # Updated prompt with more specific instructions
    # prompt = f"Translate the user requirements: {requirements}, and generate additional business related questions required for software development based on these requirements.Note: The questions should be formatted as a Python dictionary with attributes and key value pair in double quotes like {output_format}"
    prompt = f"As a software development firm, we aim to better understand your requirements for the project related to {requirements}. Please provide us with additional insights and details that will help us tailor our approach to meet your business needs. We will frame our questions in a way that is easy to understand for non-technical clients.  Please generate 10 questions. if its a technical question, please provide some recommended one word answers. here is the output format for the questions: {output_format}."
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

    requirements["detailed_requirements"] = detailed_requirements

    # output_format = {
    #     "project": {
    #         "name": "",
    #         "description": "",
    #         "requirements": {
    #             "target_platforms": "",
    #             "backend_required": "",
    #             "description": "",
    #         },
    #     }}
    # prompt = f"convert question answers : {detailed_requirements} into more business requirements. Combine all project requirements including: {requirements}, and make one single python dictionary containing all requirements like {output_format}. Also add more information in detailed requirements that might be essential for such projects additional to the requirements provided by the user. "
    # # prompt = f"recreate the following requirements:  \"{requirements}\" and add the detailed requirements in it in clear and more details based on. also add the detailed requirement with the key 'details'. Output should be in python dictionary format like the original requirement format.use double quotes for keys and values."

    # response = createResponse(prompt)

    # print(" response final:", response)
    # parsed_response = ast.literal_eval(response)

    return requirements


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
