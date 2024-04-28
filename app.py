import streamlit as st
from pages.chatbot import run_bot
import database

import streamlit as st
from time import sleep


st.title("Welcome to SerenityBot")
st.image('logo.png', width=500, use_column_width=None, clamp=True, channels="RGB", output_format="auto")

st.write("Please log in to continue.")

username = st.text_input("Please Enter your name")

if st.button("Log in", type="primary"):
    if len(username) > 0 and username == username:
        st.session_state.logged_in = True
        hist = database.fetch_user_hist(username)

        st.success("Logged in successfully!")
        sleep(0.5)
        st.session_state['username'] = username
        st.session_state['hist'] = hist
        st.switch_page("pages/chatbot.py")

    else:
        st.error("Empty name")

