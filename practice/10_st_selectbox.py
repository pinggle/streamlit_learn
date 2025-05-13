import streamlit as st
st.header('st.selectbox')
option=st.selectbox(
    label='What is your favorite color?',
    options=('Red','Green','Blue')    
)
st.write('Your favorite color is ', option)