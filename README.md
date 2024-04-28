# serenity_bot

<img src="https://github.com/naserahmadi/serenity_bot/assets/45039751/dcedf8fb-b072-4267-9087-4801ba9d0822" width="100" height="100">

This repository contains the code for **serenity bot**. Serenity is a therapist chatbot that helps customer in anger management, stress relief, etc. 
The chatbot was built based on ``streamlit`` and ``ollama``. 
For running the code: 
- Install required packages by running ``pip install -r requirements.txt``.
- Install ``ollama`` on your machine: ``curl -fsSL https://ollama.com/install.sh | sh``
- Pull the llm that you want to use as the base model. The model should be selected based on the machine that the code is running on. For example: ``ollama run command-r:35b-v0.1-fp16`` or ``ollama run llama3:70b``. You can easily change your llm in the chatbot ui. For adding a new base model, first pull the model from `ollama` and then change the model in the drop-down menu in streamlit.  
- Run the application: ``streamlit run app.py``.
  
## How chatbot manages history?
After each conversation (when the user logged out from the system). We ask the chatbot to create a report from the previous conversation (a report which contains the information and symptoms related to the current user). This infomation are stored in ``users`` folder. 
Before starting each session we check ``users'' folder to see if we can retireve any report about the current user. If there is a report we pass it to the chatbot. 

## Chatbot evaluation
In the current version, we deployed the easiest way to evaluate our chatbot: asking user to rate the chatbot (from 1 to 5) and this data is stored in the users preferences.
Some other methods can be done for the evaluation:
- Use stronger models (e.g. **GPT-4** or **llama3-70**) to give a score to the output of the chatbot.
- Training a reference model (e.g. *Prometheus*) is another option which will be expensive.
- Use real or synthetic data from conversations between a therapist and a patient and see how good our model performs on those scenarios. We can create these scenarios from real cases or prompt a strong model like GPT-4 for creating those scenarios. These scenarios should be in chat format.  

![image](https://github.com/naserahmadi/serenity_bot/assets/45039751/0eaac3eb-78e5-453a-b7eb-9742bf557c4d)
