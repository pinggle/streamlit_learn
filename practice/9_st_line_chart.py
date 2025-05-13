import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.header('Line chart')

# 随机生成的数字，组成三列数据;
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.write("chart_data原始数据为:",chart_data.T)
st.write("chart_data使用st.line_chart展示折线图效果如下:")
# 使用 st.line_chart() 创建一个折线图,使用 chart_data作为输入数据;
st.line_chart(data=chart_data)

# st.altair_chart 显示散点图;
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(chart_data)
        .mark_circle()
        .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)
st.write("chart_data使用st.altair_chart展示散点图效果如下:")
st.altair_chart(c, use_container_width=True)