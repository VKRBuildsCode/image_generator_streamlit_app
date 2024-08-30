import streamlit as st
from streamlit_toggle import toggle
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.title('Streamlit Toggle')
toggle()