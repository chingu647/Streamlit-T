import streamlit as st 
import pandas as pd
import numpy as np
import time
import os
from datetime import datetime
from collections import Counter
from PIL import Image 

def run_tab():
    st.markdown("###### 가설2 : 직전 6개년간 `서울시 구별 평균 아파트 실거래가(매매가격)의 순위`에 차이가 있다.") 

    img2 = Image.open('imgs/graph_02.png')
    st.image(img2)

    st.markdown("###### 결론 : 직전 6개년간 `서울시 구별 평균 아파트 실거래가의 순위`는 일부 차이가 있었습니다.") 
    st.markdown(r"""
	1.  **시각화 결과** 과거 3년간(2018~2020) 서울시의 구별 아파트 실거래가격은 `증가 추세`였으며,
		이후 3년간(2021년 ~ 2023년) 아파트 실거래가격은 `보합 및 하락 추세` 로 판단됩니다.
		*  **순위 상승** : 용산구(4->3위), 강동구, 영등포구, 양천구, 종로구 등
		* 순위 하락 : 중구(9 -> 11위), 강서구(14->15위), 관악구(17->19위) 등
	2. 참고로, 부동산 거래량은 2022년 최저 수준, 2023년은 2018년 대비 40% 수준입니다.
		* 2018년(81,656건)
		* 2019년(75,082건)
		* 2020년(84,140건)
		* 2021년(43,464건)
		* 2022년(12,735건)
		* 2023년(32,918건)
    """) 
