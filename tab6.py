import streamlit as st 
import pandas as pd
import numpy as np
import time
import os
from datetime import datetime
from collections import Counter
from PIL import Image 

def run_tab():
    st.markdown("####  3가지 가설에 대해 아래의 결과를 확인하였습니다.")
    st.markdown("######  1. 직전 5개년간 `서울시 구별 평균 개별공시지가 순위`는 차이는 없었습니다.")
    st.markdown("######  2. 직전 6개년간 `서울시 구별 평균 아파트 실거래가의 순위`는 일부 차이가 있었습니다.")

    st.markdown("######  3. `서울시 구별 평균 아파트 실거래가'`는 서울시 구별 `인프라 수준`과 관계가 크게 없었습니다.")
    st.markdown(r"""
	- **회귀분석 결과** `2023년도 서울시 아파트 실거래가`는 **구별 인프라 수준**보다는 < **과거 시세** >와 높은 관계가 있었습니다.
	- 서울시 아파트 실거래가 예측을 위해,  
		* 과거 시세변동 데이터 시각화를 통한 추세분석 및 지하철역 개수 및 외국인 학교 수를 참고할 필요가 있습니다.
	- 본 프로젝트는 **데이터 부족(25개 row) 한계점**이 있습니다.
		* 구 단위의 자료인 row 25개를 복사(pd.concat)하여 500개로 만들어 프로젝트를 진행한 결과 / mape는 zero 수준으로 나타났습니다. / 그 의미는 ?
		* 동 단위의 자료로 row를 확대하여 추가 판단이 필요하다고 생각됩니다.
    """)
    st.markdown("""---""")
