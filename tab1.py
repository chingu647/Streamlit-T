import streamlit as st 
import pandas as pd
import numpy as np
import time
import os
from datetime import datetime
from collections import Counter
from PIL import Image 

def run_tab():
    st.markdown(r"""
	**1. (개인적으로) 프로젝트 수행시 잘못한 점**
	- 가설 미수립하고 주어진 데이터 분석을 진행함
		* 서울시 개별공시지가 는 의미없는 자료 였습니다.
		* 내용은... 가설1로 하였습니다.
	- 데이터 전처리시 결측값 체크 및 수정 없이 진행함.
		* 문자열 split() 등 사용시 에러가 발생했습니다.

	**2. (프로젝트 해보니) 미흡한 점**
	- 실제 해보려고 하니, 함수가 잘 기억이 나지 않았습니다.
	- 프로젝트 주제 선정의 어려움 
		* 어려운 주제보다는 탐색적 데이터 분석 중심으로 프로젝트를 진행 하였습니다.
	- 본 프로젝트는 **데이터 부족(25개 row) 한계점**이 있었습니다. 
		* row자료가 너무 적었음 : 서울시 25개 군별로 분석하였는데, 자료(row)수가 너무 적었고 생각되었습니다.
		* **자료 숫자를 늘리기 위해서 중복 데이터를 만들어 프로젝트를 진행하였습니다.** (25개 -> 500개)
		* 인프라의 내용에 `외국인 거주자 수`, `기업체 수` 등 도 포함 시킬 필요가 있다고 생각됩니다.

	**3. (pycaret 수행시) 궁금했던 점 들**
	- plot_model(estimator = tuned_model, plot = 'learning')에서 training_score 하락이 의미하는 이유는 무엇인지 궁금하였습니다 ? 
		* row 갯수 부족 때문 인가요 ? 
	- plot_model(model)에서
		* cross_validation_score가 보이지 않았습니다.  
		* row 갯수를 늘려주니(여기서는 데이터 복사) 점수가 높아져서 인지.... 드디어 나타났습니다.  
    """)
