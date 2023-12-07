import streamlit as st 
import pandas as pd
import numpy as np

import time
import os

from datetime import datetime
from collections import Counter

from PIL import Image 

st.markdown(r"""###서울시 아파트 가격 추세 분석 및 회귀모델 분석""") 
st.markdown("""---""") 

tab_titles = ['Project 개요', '느낀점', 'Project 절차', 'Project 3가지', '가설 1', '가설 2', '가설 3', 'Data source']
tabs = st.tabs(tab_titles)
 
# 각 탭에 콘텐츠 추가
with tabs[0]: 
    st.markdown(r"""
	1. 현대 사회에서 부동산은 모든 사람들의 관심사항이 되었으며, 특히 서울시 소재 부동산 가격에 대한 관심은 매우 크다고 할 수 있습니다.
	2. 이번 프로젝트에서는 서울시 구별로 부동산 가격차이를 데이터 시각화를 통해 알아보고, 회귀모델을 통해 주요 원인을 찾아보고자 합니다.
    """)
 
with tabs[1]:
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
		*어려운 주제보다는 탐색적 데이터 분석 중심으로 프로젝트를 진행 하였습니다.
	- 본 프로젝트는 **데이터 부족(25개 row) 한계점**이 있었습니다.**
		* row자료가 너무 적었음 : 서울시 25개 군별로 분석하였는데, 자료(row)수가 너무 적었고 생각되었습니다.
		* **자료 숫자를 늘리기 위해서 중복 데이터를 만들어 프로젝트를 진행하였습니다.** (25개 -> 500개)
		* 인프라의 내용에 `외국인 거주자 수`, `기업체 수` 등 도 포함 시킬 필요가 있다고 생각됩니다.

	**3. (pycaret 수행시) 궁금했던 점 들**
	- plot_model(estimator = tuned_model, plot = 'learning')에서 training_score 하락이 의미하는 이유는 무엇인지 궁금합니다 ? 
		* row 갯수 부족 때문 인가요 ? 
	- plot_model(model)에서
		* cross_validation_score가 보이지 않았습니다.  
		* row 갯수를 늘려주니(여기서는 데이터 복사) 점수가 높아져서 인지.... 드디어 나타났습니다.  
    """)

with tabs[2]:
    st.header('Project 절차')
    st.write('여기서 데이터를 시각화합니다...')

with tabs[3]:
    st.markdown(r"""
	다음의 3가지 가설을 확인하고자 합니다.
	- [가설 1] : **직전 5개년간 `서울시 구별 평균 개별공시지가 순위`에 차이가 있다.**
		* 개별공시지가 : 지자체가 세금결정을 위해 매년 발표하는 1㎡당 토지단가(원/㎡)입니다.
		* 검증 방법 : 데이터 시각화를 통한 확인

	- [가설 2] : **직전 6개년간 `서울시 구별 평균 아파트 실거래가의 순위`에 차이가 있다.**
		* 아파트 실거래가 : 국토교통부 실거래가 공개시스템 자료
		* 검증 방법 : 데이터 시각화를 통한 확인

	- [가설 3] : **`서울시 구별 평균 아파트 실거래가`는 서울시 구별 인프라 수준과 관계가 있다.**
		* 서울시 구별 인프라 : 병원수, (초,중,고)학교수, 도서관 수, 지하철역 수, 버스정류장 수
		* 검증 방법 : 회귀모델을 통한 데이터 분석
    """)

with tabs[4]:
    st.header('가설 1 분석')
    st.write('여기서 데이터를 시각화합니다...')

with tabs[5]:
    st.header('가설 2 분석')
    st.write('여기서 데이터를 시각화합니다...')

with tabs[6]:
    st.header('가설 2 분석')
    st.write('여기서 데이터를 시각화합니다...')

with tabs[7]:
    st.markdown(r"""
	- 자료 1. 매년 토지소재지 자치구청장이 개별공시지가를 공개합니다. (링크: http://data.seoul.go.kr/dataList/OA-1180/F/1/datasetView.do)
		* 개별공시지가 : 결정공시하는 1㎡당 토지단가(원/㎡)입니다.

	- 자료 2. 국토교통부 제공 아파트 실거래가 자료 (링크: http://rtdown.molit.go.kr/)
		* 부동산 거래신고등 법률에 따라 등록된 계약일 기준 실거래가격 정보

	- 자료 3. 서울시 소재 병원은 881개가 있습니다. (링크: https://data.seoul.go.kr/dataList/OA-16479/S/1/datasetView.do)

	- 자료 4. 서울시 소재 학교는 총 3,932개가 있습니다. (링크: https://data.seoul.go.kr/dataList/199/S/2/datasetView.do)

	- 자료 5. 서울시 소재 도서관은 총 537개 가 있습니다. (링크: https://data.seoul.go.kr/dataList/387/S/2/datasetView.do)

	- 자료 6. 서울시 소재 지하철역은 총 288개 가 있습니다. (링크: https://www.data.go.kr/data/15081868/fileData.do)

	- 자료 7. 서울시 소재 버스정류장은 총 430개 가 있습니다. (링크: https://data.seoul.go.kr/dataList/OA-21225/S/1/datasetView.do)
    """)
 

with tabs[7]:
    st.header('가설 3 분석')
    st.write('여기서 데이터를 시각화합니다...')