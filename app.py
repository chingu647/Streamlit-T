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

tab_titles = ['Project 개요', 'Project 후기', 'Data source', 'Project 절차', 'Project 3가지', '가설 1', '가설 2', '가설 3']
tabs = st.tabs(tab_titles)
 
# 각 탭에 콘텐츠 추가
with tabs[0]: 
    st.header('Project 개요')
    st.write('여기서 데이터를 로드합니다...')
 
with tabs[1]:
    st.header('Project 후기')
    st.write('여기서 데이터를 정리합니다...')
 
with tabs[2]:
    st.header('Data source')
    st.write('여기서 데이터를 분석합니다...')
 
with tabs[3]:
    st.header('Project 절차')
    st.write('여기서 데이터를 시각화합니다...')

with tabs[4]:
    st.header('Project 3가지')
    st.write('여기서 데이터를 시각화합니다...')

with tabs[5]:
    st.header('가설 1')
    st.write('여기서 데이터를 시각화합니다...')

with tabs[6]:
    st.header('가설 2')
    st.write('여기서 데이터를 시각화합니다...')

with tabs[7]:
    st.header('가설 3')
    st.write('여기서 데이터를 시각화합니다...')