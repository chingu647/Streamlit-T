import streamlit as st 
import pandas as pd
import numpy as np

import time
import os

from datetime import datetime
from collections import Counter

from PIL import Image 

st.header("서울시 아파트 가격 추세 분석 및 회귀분석")
st.markdown("""---""") 

tab_titles = ['Data Loading', 'Data Cleaning', 'Data Analysis', 'Data Visualization']
tabs = st.tabs(tab_titles)
 
# 각 탭에 콘텐츠 추가
with tabs[0]: 
    st.header('데이터 로딩')
    st.write('여기서 데이터를 로드합니다...')
 
with tabs[1]:
    st.header('데이터 클리닝')
    st.write('여기서 데이터를 정리합니다...')
 
with tabs[2]:
    st.header('데이터 분석')
    st.write('여기서 데이터를 분석합니다...')
 
with tabs[3]:
    st.header('데이터 시각화')
    st.write('여기서 데이터를 시각화합니다...')