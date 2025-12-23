from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

llm = Ollama(model="llama3.1")

prompt = PromptTemplate(
    input_variables=["resume", "job"],
    template="""
You are an expert career coach.

Resume:
{resume}

Job Description:
{job}

Tasks:
1. Calculate skill match percentage
2. List matched skills
3. List missing skills
4. Give resume improvement suggestions

Respond in clear bullet points.
"""
)

def analyze(resume_text, job_text):
    return llm(prompt.format(resume=resume_text, job=job_text))
