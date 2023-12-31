import streamlit as st 
import pandas as pd
import numpy as np
import time
import os
from datetime import datetime
from collections import Counter
from PIL import Image 

def run_tab():
    st.markdown("###### 가설1 : 직전 5개년간 `서울시 구별 평균 개별공시지가 순위`에 차이가 있다.") 

    img = Image.open('imgs/graph_01.png')
    st.image(img)

    st.markdown("###### 결론 : 직전 5개년간 `서울시 구별 평균 개별공시지가 순위`에 차이는 없었습니다.") 
    st.markdown(r"""
	1.  **시각화 결과** 과거 5년간(2019년 ~ 2023년) 서울시의 `개별공시지가 순위`는 구별로 변화가 없었습니다.
	2. 서울시 구별 개별공시지가 순위는 시간의 변화에 따라 변화가 없다고 판단됩니다.
    """)
