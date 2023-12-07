import streamlit as st 

import pandas as pd
import numpy as np
import time
import os
from datetime import datetime
from collections import Counter

from PIL import Image 

import tab0.py
import tab1.py 
import tab2.py 
import tab3.py 
import tab4.py 
import tab5.py 
import tab6.py 
import tab7.py 

st.markdown("#### 서울시 아파트 가격 추세 분석 및 회귀모델 분석") 
st.markdown("""---""") 

tab_titles = ['Project 개요', '느낀점 부터', 'Project 가설 3가지', '가설1 분석', '가설2 분석', '가설3 분석', '결 론', 'Data source']
tabs = st.tabs(tab_titles)
 
# 각 탭에 콘텐츠 추가
with tabs[0]: 
    tab0.run_tab()
 
with tabs[1]:
    tab1.run_tab()

with tabs[2]:
    tab2.run_tab()

with tabs[3]: 
    tab3.run_tab()

with tabs[4]:
    tab4.run_tab() 

with tabs[5]:
    tab5.run_tab()

with tabs[6]:
    tab6.run_tab()

with tabs[7]:
    tab7.run_tab()
