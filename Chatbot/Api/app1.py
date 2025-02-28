from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langserve import add_routes
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Llama 2 API",
    version="1.0",
    description="API for interacting with Llama 2 via Ollama",
)

# Pydantic model for request body, now includes language
class QueryRequest(BaseModel):
    query: str
    language: str = "en" # Default language is English

# Initialize Ollama and Llama 2
try:
    llm = Ollama(model="mistral")
except ValueError as e:
    raise HTTPException(status_code=500, detail=f"Ollama initialization failed: {e}. Ensure Ollama is running and Llama 2 is pulled.")

# Prompt templates dictionary
prompt_templates = {
    "en": "Provide an answer for the given query: {query} in English for user understanding.",
"mr": "प्रश्न:{query} चं उत्तर मराठी भाषेत द्या. ते ग्रामॅटिकली करेक्ट असावं आणि समजायला सोपं असावं.  गुंतागुंतीची वाक्यं नको, सोप्या भाषेत लिहा.",
    "hi": "Provide an answer for the given query: {query} in Hindi (Devanagari script) for user understanding.",
}

# Langchain chain function (now language-aware)
def create_chain(language: str):
    prompt_template = prompt_templates.get(language, prompt_templates["en"]) # Default to English if language not found
    prompt = ChatPromptTemplate.from_template(f"[INST] {prompt_template} [/INST]")
    chain = prompt | llm
    return chain

# Langserve routes (using default English chain initially, can be adapted for language in path if needed)
add_routes(
    app,
    create_chain("en"), # Default English chain for langserve path
    path="/query",
)

# Manual endpoint (alternative to Langserve's auto-generated routes) - now language-aware
@app.post("/manual_query")
async def manual_query(request: QueryRequest):
    try:
        chain = create_chain(request.language) # Create chain based on requested language
        result = chain.invoke({"query": request.query})
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)