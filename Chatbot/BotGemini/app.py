from google import genai
from PIL import Image
import io #import io to convert image to bytes.

client = genai.Client(api_key="AIzaSyBzEg9vjzDDA-dnrjauXBzz1nmdwPV-ojA")

def model (intput_text):
    response=client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[intput_text]
    )

    return response




# response = client.models.generate_content(
#     model="gemini-2.0-flash",
#     contents=[image, "genrate a json object in which there will the be the key which are shown in investigation and the result as the value for that key."])
response = model(image,"genrate a json object in which there will the be the key which are shown in investigation and the result as the value for that key and give the title of image as object name .")
print(response.text)
