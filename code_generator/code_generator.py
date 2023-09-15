import json

# Load the templates from a JSON file
with open("templates.json", "r") as file:
    templates = json.load(file)

# User input
language = input(
    "Enter the target programming language (python, javascript, java, cpp): ").lower()
template_identifier = input(
    "Enter the template identifier (e.g., 'simple', 'initialize_none', 'var', 'let'): ")

# Check if the selected language exists in the templates
if language in templates:
    # Check if the template identifier exists for the selected language
    if template_identifier in templates[language]["variable_declaration"]:
        selected_template = templates[language]["variable_declaration"][template_identifier]
        variable_name = input("Enter the variable name: ")
        variable_value = input("Enter the variable value: ")

        # Replace placeholders with user-provided values
        generated_code = selected_template.replace(
            "variable_name", variable_name).replace("variable_value", variable_value)
        print(generated_code)
    else:
        print("Invalid template identifier")
else:
    print("Unsupported language")
