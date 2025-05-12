import streamlit as st

# https://30days.streamlit.app/?challenge=Day3

# 应用的标题文字;
st.header('st.button')
# 使用条件分支语句 if 和 else 来显示不同的消息;
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')