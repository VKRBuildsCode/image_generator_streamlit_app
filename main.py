import streamlit as st
st.set_page_config(page_title="IMGGen",page_icon="❤️")
st.title("kalyan ram")
choice=st.sidebar.selectbox("Select your choice",["Home","DALL-E","Diffusers"])
hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)