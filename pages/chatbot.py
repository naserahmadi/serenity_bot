import os
import streamlit as st
from prompt import MAIN_PROMPT, CHAT_HISTORY, SUMMARIZE_PROMPT
import ollama
import database


st.session_state['model'] = 'command-r:35b-v0.1-fp16'

def run_bot():
    user = st.session_state['username']
    hist = database.fetch_user_hist(user)
    st.title(f"Welcome to SerenityBot Dear {user}")

    models = [o['name'] for o in ollama.list()['models']]
    defualt_model = 'command-r:35b-v0.1-fp16'

    model_name = st.selectbox(
        '**Please select the LLM model you want to use**', models, 
        index= models.index(defualt_model) )
    
    st.session_state['model'] = model_name
    if st.sidebar.button("Logout", type="primary"):
        logout()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("How can i help you today?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        main_prompt = MAIN_PROMPT
        if len(hist) > 0:
            main_prompt += CHAT_HISTORY.format(HIST=hist)

        chat_history=[{'role': 'system', 'content': main_prompt}]
        

        for m in st.session_state.messages:
            chat_history.append(m)
            
        with st.chat_message("assistant"):
            message_placeholder = st.empty()

            chat_history.append({'role': 'user', 'content': prompt})
            stream = ollama.chat(
                model=model_name,
                messages=chat_history,
                stream=True,
                options = {'temperature': 0 }
            )

            full_response = ""
            for response in stream:
                full_response += response['message']['content']
                message_placeholder.markdown((full_response + "▌"))
            message_placeholder.markdown(full_response)
        chat_history.append({'role': 'assistant', 'content': full_response})
        st.session_state.messages.append({"role": "assistant", "content": full_response})
        from streamlit_star_rating import st_star_rating
        st.session_state['star'] = st_star_rating("Please rate you experience", maxValue=5, defaultValue=3, key="rating", on_click=star_click)


def star_click(value):
    st.session_state['star'] = value


def logout():
    chat_history_summ=[]
    for m in st.session_state.messages:
        if m['role'] != 'system':
            chat_history_summ.append(m)

    chat_history_summ.append({'role': 'system', 'content': SUMMARIZE_PROMPT})
    sum = ollama.chat(model=st.session_state['model'],
            messages=chat_history_summ,
            stream=False,
            options = {'temperature': 0 }
        )

    database.update_sum(st.session_state['username'], sum['message']['content'], st.session_state['star'])
    st.warning('you are logged out!')


if __name__=='__main__':
    run_bot()
