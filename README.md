# Chatbot
This repository having a chatbot's by using laama which is open source model, then gemini ai api used, then i created it's api's using a Fastapi and then also created the user interface using Streamlit and integret both and working perfectly.


# Llama Folder

using venv as virtual environment.

##
 <tab><tab>code/conda activate venv

Folder having only one file app.py which having the code of basic implementation of llama model.

# Api 
Api folder containing the app.py having the api created using fastapi and in whihc I have use a llama mode for solving my quries.
in app1.py having a same code but trying to get output in multilanguage in marathi,hindi,english,etc firstly i used the llama but it is not that efficient for multilanguage question answering, so then I use the mistral model download from Ollama and then it is giving output in multilanguage but it is not that much sematically correct.

# BotGemini

using Botenv as virtual environemt

- conda activate Botenv
  
In this folder having multiple apis app.py having basic implementation of gemini ai which takes query and image as input,

Then app1.py having a same gemini ai model which takes a query and image as input and prvoide the details, currently it is not working for the query+image together but it is providing accurate data inside of image and also having code to do post request to express backend to store the data into the mongo db that storing id also get as output on ui client.py.

In app2.py having gemini model which respons the query entered by user from client2.py.

# commands 

If file containing the code of rest api use command :

- python file_name.py

If file containing the code of stramlit the use command :

- stramlit run file_name.py


