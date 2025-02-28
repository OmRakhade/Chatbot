from fastapi import FastAPI, HTTPException
from google import genai

app = FastAPI()

# Initialize the Gemini client (replace with your actual API key)
client = genai.Client(api_key="AIzaSyBzEg9vjzDDA-dnrjauXBzz1nmdwPV-ojA")

def get_gemini_text_response(query: str):
    """Gets the Gemini response for a text query."""
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=query
        )
        return response.text
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query/")
async def query_gemini(query: str):
    """Handles text queries and returns the result."""
    try:
        gemini_response = get_gemini_text_response(query)
        return gemini_response #returning plain text.
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)