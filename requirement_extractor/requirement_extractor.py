import os
import openai


def initiate():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Initialize an empty dictionary to store the requirements
    project = {
        "name": "",
        "description": "",
        "requirements": {
            "target_platforms": "",
            "frontend_required": "",
            "backend_required": "",
            "description": "",
        },
        "additional_notes": ""
    }

    done = False
    while not done:
        project["name"] = input("Enter project name: ")
        if len(project["name"]) > 2:
            done = True

    done = False
    while not done:
        project["description"] = input("Enter project description: ")
        if len(project["description"]) > 5:
            done = True

    # done = False
    # while not done:
    #     project["client_info"]['name'] = input("Enter Client's Name: ")
    #     if len(project["client_info"]['name']) > 5:
    #         done = True

    # done = False
    # while not done:
    #     project["client_info"]['email'] = input("Enter Client's Email: ")
    #     if len(project["client_info"]['email']) > 5:
    #         done = True

    # done = False
    # while not done:
    #     project["client_info"]['phone'] = input(
    #         "Enter Client's Phone Number: ")
    #     if len(project["client_info"]['phone']) > 5:
    #         done = True

    done = False
    while not done:
        target_platforms = input(
            "Enter targeted platform(s) (comma-separated, e.g., Web, Mobile, Desktop): ")

        platforms = [platform.strip().capitalize()
                     for platform in target_platforms.split(",")]

        valid_platforms = ["Web", "Mobile", "Desktop"]

        if all(platform in valid_platforms for platform in platforms):
            project["requirements"]["target_platforms"] = platforms
            done = True
        else:
            print(
                "Invalid platform(s). Please use 'Web', 'Mobile', 'Desktop' or combinations.")

    done = False
    while not done:
        user_input = input("Is a Frontend required? (yes/no): ").lower()
        if user_input in ["yes", "no"]:
            project["requirements"]["frontend_required"] = (
                user_input == 'yes')
            done = True
        else:
            print("Please enter 'yes' or 'no'.")

    done = False
    while not done:
        user_input = input("Is a backend required? (yes/no): ").lower()
        if user_input in ["yes", "no"]:
            project["requirements"]["backend_required"] = (
                user_input == 'yes')
            done = True
        else:
            print("Please enter 'yes' or 'no'.")

    if project["requirements"]["frontend_required"] == False and project["requirements"]["backend_required"] == False:
        print("Invalid Input: Atleast one of the frontend or backend is required")
        done = False
        while not done:
            user_input = input("Is a Frontend required? (yes/no): ").lower()
            if user_input in ["yes", "no"]:
                project["requirements"]["frontend_required"] = (
                    user_input == 'yes')
                done = True
            else:
                print("Please enter 'yes' or 'no'.")

        done = False
        while not done:
            user_input = input("Is a backend required? (yes/no): ").lower()
            if user_input in ["yes", "no"]:
                project["requirements"]["backend_required"] = (
                    user_input == 'yes')
                done = True
            else:
                print("Please enter 'yes' or 'no'.")

    done = False
    while not done:
        project["requirements"]["description"] = input(
            "Enter project requirements: ")
        if len(project["requirements"]["description"]) > 5:
            done = True

    # done = False
    # while not done:
    #     project["deadline"] = input("Enter project deadline: ")
    #     if len(project["deadline"]) > 5:
    #         done = True

    # done = False
    # while not done:
    #     project["budget"] = input("Enter project budget: ")
    #     if len(project["budget"]) > 1:
    #         done = True

    done = False
    while not done:
        project["additional_notes"] = input("Enter additional notes: ")
        if len(project["additional_notes"]) > 1:
            done = True

    return project

    # for key, value in fields.items():
    #     if isinstance(value, dict):
    #         print(key)
    #         for subkey, subvalue in value.items():
    #             print(subkey)
    #     else:
    #         print(key, value)

    # done = True
#             # Check if the field is missing in the requirements dictionary
#             if field not in requirements:
#                 # Prompt the user for the missing information
#                 user_input = input(f"Please provide {field}: ")

#                 # Update the requirements dictionary with user input
#                 requirements[field] = user_input

#                 # Mark the field as answered
#                 answered_fields.add(field)

#     # Ask if backend is needed
#     while True:
#         backend_required = input("Is a backend required? (yes/no): ").lower()
#         if backend_required in ["yes", "no"]:
#             requirements["requirements"] = {
#                 "backend_required": (backend_required == 'yes')
#             }
#             break
#         else:
#             print("Please enter 'yes' or 'no'.")

#     # Ask for target platforms
#     while True:
#         target_platforms = input(
#             "Enter targeted platform(s) (comma-separated, e.g., Web, Mobile, Desktop): ")
#         platforms = [platform.strip()
#                      for platform in target_platforms.split(",")]
#         valid_platforms = ["Web", "Mobile", "Desktop"]

#         if all(platform in valid_platforms for platform in platforms):
#             requirements["requirements"]["target_platforms"] = platforms
#             break
#         else:
#             print(
#                 "Invalid platform(s). Please use 'Web', 'Mobile', 'Desktop' or combinations.")

#     # Once all required fields are filled, return the complete requirements
#     return requirements


# # # Example usage
# # if __name__ == "__main__":
# #     software_requirements = analyze()
# #     print("Software Requirements:")
# #     print(json.dumps(software_requirements, indent=2))

# #
# # import os
# # import openai
# # import json


# # def analyze(request):
# #     print("analyze")

# #     openai.api_key = os.getenv("OPENAI_API_KEY")

# #     # Updated prompt with more specific instructions
# #     prompt = f"Translate the user request \"{request}\" into structured software development requirements in JSON format. Include project_name, project_description, client_info, requirements, deadline, budget, and any additional_notes. You may also ask for any missing details."

# #     response = openai.Completion.create(
# #         model="text-davinci-003",
# #         prompt=prompt,
# #         temperature=0.7,  # Adjust temperature for desired creativity
# #         max_tokens=300,    # Adjust max_tokens based on desired response length
# #         top_p=1.0,
# #         frequency_penalty=0.0,
# #         presence_penalty=0.0
# #     )

# #     # try:
# #     #     # Attempt to parse the AI response as JSON
# #     #     print(f"response: {response}")
# #     #     parsed_response = json.loads(response.choices[0].text)
# #     # except json.JSONDecodeError as e:
# #     #     parsed_response = {"error": "Failed to parse AI response as JSON",
# #     #                        "raw_response": response.choices[0].text}

# #     return response.choices[0].text
