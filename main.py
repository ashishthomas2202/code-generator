import json
from dotenv import load_dotenv
import requirement_extractor as re
import requirement_analyzer as ra
import design_analyzer as da
import code_generator as cg


# Load environment variables
load_dotenv()


def main():

    project = re.initiate()
    # project = {
    #     "name": "Rolls Royce",
    #     "description": "Its a Luxury Car Brand",
    #     "requirements": {
    #         "target_platforms": ["Web", "Mobile", "Desktop"],
    #         "frontend_required": True,
    #         "backend_required": True,
    #         "description": "Needs Ecommerce Functionality",
    #     },
    #     "additional_notes": "Minimal Design"
    # }

    project["detailed_requirements"] = ra.analyze(project)

    # project = {
    #     "name": "Rolls Royce",
    #     "description": "Its a Luxury Car Brand",
    #     "requirements": {
    #         "target_platforms": [
    #             "Web",
    #             "Mobile",
    #             "Desktop"
    #         ],
    #         "frontend_required": True,
    #         "backend_required": True,
    #         "description": "Needs Ecommerce Functionality"
    #     },
    #     "additional_notes": "Minimal Design",
    #     "detailed_requirements": [
    #         {
    #             "question": "What is the estimated budget for the project?",
    #             "answer": "10000"
    #         },
    #         {
    #             "question": "To what platforms would you like the project to be available? (Web, Mobile, Desktop)",
    #             "answer": "ALL"
    #         },
    #         {
    #             "question": "Which features are absolutely necessary for the design?",
    #             "answer": "user authentication,admin dashboard, user dashboard"
    #         },
    #         {
    #             "question": "What type of interface would you like? (Minimal design)",
    #             "answer": "Minimal but luxurious"
    #         },
    #         {
    #             "question": "What type of user functionalities are needed? (ecommerce functionality)",
    #             "answer": "Authentication, payment gateway, order management for admin"
    #         },
    #         {
    #             "question": "Do you already have a domain name or server for the project? [Yes/No]",
    #             "answer": "no"
    #         },
    #         {
    #             "question": "Would you consider using third-party services to facilitate development? [Yes/No]",
    #             "answer": "no"
    #         },
    #         {
    #             "question": "Are these changes proposed to be short-term or long-term?",
    #             "answer": "long term"
    #         },
    #         {
    #             "question": "Do you have existing visual style and guidelines for the project? [Yes/No]",
    #             "answer": "No"
    #         },
    #         {
    #             "question": "What type of testing do you require the project to pass through? (e.g. Quality Assurance, User Testing)",
    #             "answer": "All"
    #         }
    #     ]
    # }

    project["design"] = da.analyze(project)

    with open("./project.json", "w") as f:
        # f.write(json.dumps(analysis))
        f.write(json.dumps(project, indent=2))

    print("Project Creation Complete!")


if __name__ == "__main__":
    main()
