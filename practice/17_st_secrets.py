import streamlit as st
st.title('st.secrets')
# It should be noted that, secrets can be stored in Streamlit Community Cloud as shown in the screenshots shown below.
# If working locally, they can be stored in .streamlit/secrets.toml, but make sure to avoid uploading this to a GitHub repo when deploying the app.
st.write(st.secrets['message'])
