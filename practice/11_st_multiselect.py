import streamlit as st
st.header('st.multiselect')
options=st.multiselect(
    label='What are your favorite colors',
    options=['Greeen','Yellow','Red','Blue'],
    default=['Yellow','Red']
)
st.write('You selected:', options)