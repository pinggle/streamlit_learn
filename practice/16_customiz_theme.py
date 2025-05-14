import streamlit as st
st.title('Customizing the theme of Streamlit apps')
st.write('Contents of the `.streamlit/config.toml` file of this app')
st.code(
"""
[theme]
primaryColor="#F39C12"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#31333F"
font="monospace"
"""
)
number=st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:',number)