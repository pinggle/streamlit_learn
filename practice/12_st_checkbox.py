import streamlit as st
st.header('st.checkbox, Display a checkbox widget.')
st.write('What would you like to order?')
icecream=st.checkbox('Ice cream')
coffee=st.checkbox('Coffee')
cola=st.checkbox('Cola')
if icecream:
    st.write("Great! Here's some more 🍦")
if coffee:
    st.write("Okay, Here's some coffee ☕️")
if cola:
    st.write("Here you go 🥤")

st.subheader('st.radio, Display a radio button widget.')
genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)
if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")