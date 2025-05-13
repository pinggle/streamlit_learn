import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

# 应用的标题文字;
st.header('st.write title')
# 样例1: 显示文字,斜体文字,字符表情;(基本用法就是显示文字和使用 Markdown 语法的文本：)
st.write('Hello, 显示斜体: *world!* 显示表情: :sunglasses:')
# 样例2: 显示数字;
st.write(1234)
# 样例3: 显示DataFrame;
df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})
st.write(df)
# 样例4: 显示文字和DataFrame,支持多个参数;
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
# 样例5: 在二维平面,按照正态分布,随机显示小圆形;
df2=pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c'])
c=alt.Chart(df2).mark_circle().encode(
    x='a',y='b',size='c',color='c',tooltip=['a','b','c']
)
st.write(c)