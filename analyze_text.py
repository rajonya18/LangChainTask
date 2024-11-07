import os
from groq import Groq
import json
from langchain_community.llms import Ollama
from langchain_ollama import ChatOllama
from crewai import Agent, Task, Crew, Process

from langchain_community.llms.huggingface_hub import HuggingFaceHub


filename = input("Enter filepath \n")

f = open(filename, 'r')
user_prompt = f.read()
f.close()


os.environ["OPENAI_API_BASE"] = "https://api.groq.com/openai/v1"
os.environ["OPENAI_MODEL_NAME"] = "llama3-70b-8192"
os.environ['OPENAI_API_KEY'] = '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'


classifier = Agent(
    role="Task Classifier",
    goal="You are supposed to understand whether the user wants to summarize a text, count the number of tokens in a text, or extract the heading from a text, or do none of these three things. Always return only 1 word. Based on the user prompt, return one of the four words: Summarize - if the user wants to summarize a text, Count - if the user wants to count the number of tokens in a text, Extract - if the user wants to extract the headings from a text, None - if the user wants to do anything else",
    backstory="You are just supposed to understand the task the user wants to do. It will one of the following - Count, Summarize, Extract, None",
    verbose = False,
    allow_delegation=False,
    

)


summarizer = Agent(
    role="Text Summarizer",
    goal="ou are supposed to get a summary of the given text within 200 words",
    backstory="You are just supposed to understand the text and give a concise summary",
    verbose = False,
    allow_delegation=False,
    

)

counter = Agent(
    role="Token Counter",
    goal="You are supposed to count the number of tokens in the mentioned text",
    backstory="The user has given an instruction to count the number of tokens in the target text. First, you need to separate the instruction from the target text. For this target text,you need to count the number of tokens",
    verbose = False,
    allow_delegation=False,
    

)

extractor = Agent(
    role="Extract Headings",
    goal="You are supposed to extract the headings and titles in the mentioned text",
    backstory="You are supposed to go through the whole text and find the headings and titles.",
    verbose = False,
    allow_delegation=False,
    

)

def split(user_input):
    _,b = user_input.split(':',1)
    return b


target_text = split(user_prompt)


classify_task = Task(
    description = f"Classify the following task - \n {user_prompt}",
    agent = classifier,
    expected_output = "One of the following four options: Count, Summarize, Extract, None",
)

summarize_task = Task(
    description = f"Summarize the following task - \n {target_text}",
    agent = summarizer,
    expected_output = "A concise summary of the target text",
)

count_task = Task(
    description = f"Count the tokens in the target string in - \n {target_text}",
    agent = counter,
    expected_output = "The number of tokens in the target text",
)

extract_task = Task(
    description = f"Extract the headings and titles from - \n {target_text}",
    agent = classifier,
    expected_output = "Headings and titles from the given text",
)



classify_crew = Crew(
    agents = [classifier],
    tasks = [classify_task],
    verbose = False,
    process = Process.sequential,
)

task = str(classify_crew.kickoff())



task_crew = None

print("-----------------------------------------------------------------------------------")
print(task)
print("-----------------------------------------------------------------------------------")


if (task=="Summarize"):
    task_crew = Crew(
        agents = [summarizer],
        tasks = [summarize_task],
        verbose = False,
        process = Process.sequential,
    )

elif (task=="Count"):
    task_crew = Crew(
        agents = [counter],
        tasks = [count_task],
        verbose = False,
        process = Process.sequential,
    )
elif(task=="Extract"):
    task_crew = Crew(
        agents = [extractor],
        tasks = [extract_task],
        verbose = False,
        process = Process.sequential,
    )
else:
    f = open("./Sample_In_Out/output_for_"+filename, "w")
    f.write("Invalid instruction for LLM")
    f.close()
    exit(0)

    

# print(task_crew.kickoff())

output = str(task_crew.kickoff())

f = open("./Sample_In_Out/output_latest.txt", "w")
f.write(output)
f.close()