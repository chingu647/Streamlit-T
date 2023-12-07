import streamlit as st 
import pandas as pd
import numpy as np

import time
import os

from datetime import datetime
from collections import Counter

from PIL import Image 

style1 = "<style>{text-align: center;}</style>"
st.markdown(style1, unsafe_allow_html=True)

col1,col2= st.columns([100,1]) 
with col1:
    st.title("2023년 인공지능 마스터 과정") 
    st.subheader("서울시 아파트 가격 추세분석 및 회귀분석") 

col3,col4 = st.columns([1,3])
with col3:
    st.title("col3-------------------------------------------------------------------------------------------------------------------------------")
with col4:
    st.title("col4-------------------------------------------------------------------------------------------------------------------------------")
    chk3 = st.checkbox("this is checkbox3") 
    chk4 = st.checkbox("this is checkbox4")       

st.sidebar.title("this is sidebar")
chk3 = st.sidebar.checkbox("체크박스 문구") 

