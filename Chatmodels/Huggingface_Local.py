## Build Chatmodel using Huggingface in local system

from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline 

llm=HuggingFacePipeline.from_model_id(
    model_id="",
    task="text-generation",
    model_kwargs={"temperature":0.1,"max_length":64}
)   

model=ChatHuggingFace(llm=llm)

res=model.invoke("What is capital of india")

print(res.content)
