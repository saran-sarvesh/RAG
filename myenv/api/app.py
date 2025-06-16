from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

app = FastAPI(
    version ="1.0",
    title = "Ollama API",
    description = "A simple API for interacting with the Ollama AI model",
)

load_dotenv()

prompt1 = ChatPromptTemplate.from_template('write essay for {topic} in 100 words')
prompt2 = ChatPromptTemplate.from_template('write poem for {topic} in 100 words')

model1 = Ollama(model="llama2")
model2 = Ollama(model="gemma3")

add_routes(
    app,
    prompt1|model1,
    path="/essay"
)

add_routes(
    app,
    prompt2|model2,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)