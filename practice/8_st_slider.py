import streamlit as st
from datetime import time,datetime

st.header('st.slider header text')
# example 1
st.subheader('Slider')
age=st.slider(label='How old are you?', min_value=0, max_value=130, value=25)
st.write("I'm ", age, ' years old')
# example 2
st.subheader('Range slider')
values=st.slider(label='Select a range of values', min_value=0.0, max_value=100.0, value=(25.0, 75.0))
st.write('Values:', values)
# The following three arguments 0.0, 100.0, (25.0, 75.0) represents the minimum and maximum values while the last tuple denotes the default values to use as the selected lower (25.0) and upper (75.0) bound values.
# example 3
st.subheader(body='Range time slider', anchor='anchor')
appointment=st.slider(label="Schedule your appointment:",value=(time(11,30), time(12,45)))
st.write("You're scheduled for:", appointment)
# example 4
st.subheader('Datetime slider')
start_time=st.slider("when do you start?", 
                     value=datetime(2025,5,1,9,30),
                     format="MM/DD/YY - hh:mm")
st.write("Start time: ", start_time)
# st.select_slider example
color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ],
)
st.write("My favorite color is", color)