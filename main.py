import os
import json
from dotenv import load_dotenv
import requirement_extractor as re
import requirement_analyzer as ra
import code_generator as cg


# Load environment variables
load_dotenv()


def main():

    # requirements = re.initiate()
    requirements = {
        "name": "Rolls Royce",
        "description": "Its a Luxury Car Brand",
        "requirements": {
            "target_platforms": ["Web", "Mobile", "Desktop"],
            "frontend_required": True,
            "backend_required": True,
            "description": "Needs Ecommerce Functionality",
        },
        "additional_notes": "Minimal Design"
    }

    refined_requirements = ra.analyze(requirements)

    with open("./requirements.json", "w") as f:
        # f.write(json.dumps(analysis))
        f.write(json.dumps(refined_requirements, indent=2))


if __name__ == "__main__":
    main()
