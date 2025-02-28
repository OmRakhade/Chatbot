from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Llama 2 API",
    version="1.0",
    description="API for interacting with Llama 2 via Ollama",
)

# Pydantic model for request body
class QueryRequest(BaseModel):
    query: str

# Initialize Ollama and Llama 2
try:
    llm = Ollama(model="llama2")
except ValueError as e:
    raise HTTPException(status_code=500, detail=f"Ollama initialization failed: {e}. Ensure Ollama is running and Llama 2 is pulled.")

# Prompt template
prompt = ChatPromptTemplate.from_template("Provide an answer for the given query: {query}")

# Langchain chain
chain = prompt | llm

# Langserve routes
add_routes(
    app,
    chain,
    path="/query",
)

# Manual endpoint (alternative to Langserve's auto-generated routes)
@app.post("/manual_query")
async def manual_query(request: QueryRequest):
    try:
        result = chain.invoke({"query": request.query})
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {e}")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)