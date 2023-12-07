import streamlit as st 
import pandas as pd
import numpy as np

import time
import os

from datetime import datetime
from collections import Counter

from PIL import Image 

def main(): 
    col1,col2 = st.columns([2,3])
    with col1:
        st.title("col1")
    with col2:
        st.title("col2")
        st.checkbox("this is checkbox1") 
        st.checkbox("this is checkbox2")       

    st.sidebar.title("this is sidebar")
    st.sidebar.checkbox("체크박스 문구")





#    st.title("서울시 아파트 가격 추세분석 및 예측")
#    name = '장인구' 
#    st.text(f"제 이름은 {name}입니다.")
#    st.header(f"이 영역은 헤더")
#    st.subheader(f"이 영역은 서브헤더")

#    st.success(f"성공했을때") 
#    st.error(f"에러일때")
#    st.warning(f"경고 일때")
#    st.info(f"정보를 줄때") 

#    st.help(sum) 
#    st.help(len)



















if __name__ == '__main__': 
    main()

