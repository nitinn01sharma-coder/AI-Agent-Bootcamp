from dotenv import load_dotenv
import os

load_dotenv()
print("Environment ready")
print("OPENAI_API_KEY exists:", bool(os.getenv("OPENAI_API_KEY")))
