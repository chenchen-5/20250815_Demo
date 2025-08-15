import numpy as np
import pandas as pd
import streamlit as st

st.title("Demo Page")
st.write("123")
st.write("# 123")

arr1 = np.array([1, 2, 3, 4, 5, 6])
st.write(arr1)

df1 = pd.DataFrame([[1, 2, 3,1234], [4, 5, 6,5678]])
st.write(df1)
st.sidebar.table(df1)

st.write("## 核取方塊")
r1 = st.checkbox("外帶")
if r1:
    st.info("外帶")
else:
    st.info("內用")

checks = st.columns(2)
txt = ''
with checks[0]:
    r11 = st.checkbox("A")
    if r11:
        txt += 'A '
with checks[1]:
    r12 = st.checkbox("B")
    if r12:
        txt += 'B '
st.info(txt)

st.write("## 單選按鈕")
r2 = st.radio("飲料", ["咖啡", "果汁", "奶茶"])
st.info(r2)
r3 = st.radio("飲料", ["咖啡", "果汁", "奶茶"],key="r3")
st.info(r3)

st.sidebar.write("滑桿")
num = st.sidebar.slider("請選擇數量:" , 0, 100, 0, 5)#(最小, 最大, 起始值, 間隔)
st.sidebar.info(num)

st.write("下拉選單")
city = st.selectbox("請選擇城市", ["台北", "台南","其他"])
if city=="台北":
    st.info("A")
elif city=="台南":
    st.info("D")
else:
    st.info("OTHERS")
#st.sidebar.功能 ---->側邊攔

st.write("按鈕")
a = st.number_input("a")
b = st.number_input("b")
if st.button("相乘"):
    st.write("### ",a * b)