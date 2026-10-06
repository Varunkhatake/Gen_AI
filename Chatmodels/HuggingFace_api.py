## build HuggingFace  Chatmodel using Api

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(
    repo_id ="",
    task="text-generation",
)

model=ChatHuggingFace(llm=llm)

res = model.invoke("What is capital of india")

print(res.content)
