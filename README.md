# serenity_bot

![image](https://github.com/naserahmadi/serenity_bot/assets/45039751/0eaac3eb-78e5-453a-b7eb-9742bf557c4d)

This repository contains the code for a therapist chatbot. 
The chatbot was built based on ``streamlit`` and ``ollama``. 
For running the code: 
- Install required packages by running ``pip install -r requirements.txt``.
- Install ``ollama`` on your machine: ``curl -fsSL https://ollama.com/install.sh | sh``
- Pull the llm that you want to use as the base model. The model should be selected based on the machine that the code is running on. For example: ``ollama run command-r:35b-v0.1-fp16`` or ``ollama run llama3:70b``. You can easily change your llm in the chatbot ui. 
- Run the application: ``streamlit run app.py``.
  
