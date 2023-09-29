
import os
from dotenv import load_dotenv
import request_analyzer as ra
import code_generator as cg

# Load environment variables
load_dotenv()


def main():
    cg.print_key()
    ra.analyze()


if __name__ == "__main__":
    main()
