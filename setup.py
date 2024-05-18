from setuptools import find_packages,setup

setup(
    name = "mcqgenerator",
    version = "0.0.1",
    author = "DKZ",
    install = ["openai","langchain","streamlit","python-dotenv","PyPDF2",
               "huggingface_hub","transformers","accelerate"],
    packages=find_packages()
)