import streamlit as st 
import pandas as pd
import numpy as np

import time
import os

from datetime import datetime
from collections import Counter

from PIL import Image 
col1,col2= st.columns([100,1])
with col1:
    st.title("col1") 

col3,col4 = st.columns([2,3])
with col3:
    st.title("col3")
with col4:
    st.title("col4")
    chk3 = st.checkbox("this is checkbox3") 
    chk4 = st.checkbox("this is checkbox4")       

st.sidebar.title("this is sidebar")
chk3 = st.sidebar.checkbox("체크박스 문구") 

