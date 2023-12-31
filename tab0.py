import streamlit as st 
import pandas as pd
import numpy as np
import time
import os
from datetime import datetime
from collections import Counter
from PIL import Image 

def run_tab(): 
    st.markdown("###### Project 개요") 
    st.markdown(r"""
	1. 현대 사회에서 부동산은 모든 사람들의 관심사항이 되었으며, 특히 서울시 소재 부동산 가격에 대한 관심은 매우 크다고 할 수 있습니다.
	2. 이번 프로젝트에서는 서울시 구별로 부동산 가격차이를 데이터 시각화를 통해 알아보고, 회귀모델을 통해 주요 원인을 찾아보고자 합니다.
    """)
    st.markdown("###### Project 절차") 
    st.markdown(r"""
	1. **데이터 확인하기 :** 데이터를 불러오고 기본 구조 확인
	2. **데이터 전처리:** 데이터 결측 확인 및 무의미한 정보 제거
	3. **데이터 분석:** 데이터 시각화 및 머신러닝 분석을 통한 가설 검증
    """)
