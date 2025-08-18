import streamlit as st
import numpy as np
import polars as pl
from io import StringIO
import json
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit_tags
from PIL import Image

st.title(':zap: pardaz-core')

banner =Image.open('./data/banner.jpeg')
st.image(banner)


login_option = st.sidebar.radio('Login/Singup', ('Login', 'Singup'))

if login_option == 'Login':


    with st.sidebar.form("Login"):
        st.write("Pardaz Core")
        user = st.text_input("Username")
        pas = st.text_input("Password")

        
        submitted = st.form_submit_button("Login")
        if submitted:
            pass
else:
    with st.sidebar.form("Signup"):
        st.write("Pardaz Core")
        user = st.text_input("Username")
        pas = st.text_input("Password")
        email = st.text_input('email')

        
        submitted = st.form_submit_button("Signup")
        if submitted:
            pass
# st.area_chart()
st.divider()


keyword = streamlit_tags.st_tags_sidebar(
    label='# Enter Keywords:',
    text='Press enter to add more',
    value=['AI', 'Python', 'pardaz'],
    suggestions=['ai', 'Ai', 'python', 
                 'git', 'gitHub', 'GitHub', 
                 'Pardaz-core', 'Pardaz'],
    maxtags = 4,
    key='2')

with st.expander('Statistics'):
    fig, ax =plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100),ax=ax)
    st.pyplot(fig)

#عکس دانلودی با گوگل
# st.image("https://thumbs.dreamstime.com/z/d-rendering-online-learning-banner-python-training-coding-concept-learn-to-code-programming-language-171308012.jpg")



with st.expander('User profile:'):
    col1, col2 = st.columns(2)
    col1.text_input('First Name:')
    col2.text_input('Last Name:')
    st.camera_input('Camera Input', key='camera_input')


st.caption('Thank you for visiting the site.')
