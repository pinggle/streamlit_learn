# https://30days.streamlit.app/?challenge=Day4
# download csv data: https://www.kaggle.com/datasets/kenjee/ken-jee-youtube-data/data

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime

# load data;
def load_data():
    df_agg = pd.read_csv('../data/Aggregated_Metrics_By_Video.csv').iloc[1:, :]
    df_add_sub = pd.read_csv(
        '../data/Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')
    df_comments = pd.read_csv('../data/All_Comments_Final.csv')
    dt_time = pd.read_csv('../data/Video_Performance_Over_Time.csv')

