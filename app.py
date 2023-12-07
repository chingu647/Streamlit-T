import streamlit as st 
import pandas as pd
import numpy as np

import time
import os

from datetime import datetime
from collections import Counter

from PIL import Image 

st.markdown("##### 서울시 아파트 가격 추세 분석 및 회귀모델 분석") 
st.markdown("""---""") 

tab_titles = ['Project 개요', '느낀점 부터', 'Project 가설 3가지', '가설1 분석', '가설2 분석', '가설3 분석', '결 론', 'Data source']
tabs = st.tabs(tab_titles)
 
# 각 탭에 콘텐츠 추가
with tabs[0]: 
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

with tabs[2]:
    st.markdown(r"""
	다음의 3가지 가설을 확인하고자 하였습니다.
	- [가설 1] : **직전 5개년간 `서울시 구별 평균 개별공시지가 순위`에 차이가 있다 ?**
		* 개별공시지가 : 지자체가 세금결정을 위해 매년 발표하는 1㎡당 토지단가(원/㎡)입니다.
		* 검증 방법 : 데이터 시각화를 통한 확인

	- [가설 2] : **직전 6개년간 `서울시 구별 평균 아파트 실거래가의 순위`에 차이가 있다 ?**
		* 아파트 실거래가 : 국토교통부 실거래가 공개시스템 자료
		* 검증 방법 : 데이터 시각화를 통한 확인

	- [가설 3] : **`서울시 구별 평균 아파트 실거래가`는 서울시 구별 인프라 수준과 관계가 있다 ?**
		* 서울시 구별 인프라 : 병원수, (초,중,고)학교수, 도서관 수, 지하철역 수, 버스정류장 수
		* 검증 방법 : 회귀모델을 통한 데이터 분석
    """)

with tabs[3]:
    st.markdown("###### 가설1 : 직전 5개년간 `서울시 구별 평균 개별공시지가 순위`에 차이가 있다.") 

    img = Image.open('graph_01.png')
    st.image(img)

    st.markdown("###### 결론 : 직전 5개년간 `서울시 구별 평균 개별공시지가 순위`에 차이는 없었습니다.") 
    st.markdown(r"""
	1.  **시각화 결과** 과거 5년간(2019년 ~ 2023년) 서울시의 `개별공시지가 순위`는 구별로 변화가 없었습니다.
	2. 서울시 구별 개별공시지가 순위는 시간의 변화에 따라 변화가 없다고 판단됩니다.
    """)

with tabs[4]:
    st.markdown("###### 가설2 : 직전 6개년간 `서울시 구별 평균 아파트 실거래가(매매가격)의 순위`에 차이가 있다.") 

    img2 = Image.open('graph_02.png')
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

with tabs[5]:
    st.markdown("###### 가설3 : `서울시 구별 평균 아파트 실거래가'는 서울시 구별 인프라 수준과 관계가 있다 ?") 


    st.markdown("###### 회귀모델별 비교") 
    img3 = Image.open('graph_03.png')
    st.image(img3)
    st.markdown(r"""
	1. 회귀모델 비교 결과 XGBRegressor 모델 성능이 가장 높게 나타났습니다.
		* Mean Absolute Percentage Error 값이 약 0.% 수준  (데이터 복사 이전 : 5.6% 수준)
	2. XGBRegressor 모델의 mape가 매우 낮아,
		* 2023년도 서울시 아파트 실제 거래가격과 
		* 예측가격 비율이 거의 일치한다고 해석됨 (데이터 복사 전 : 5.6% 차이)
    """)
    st.markdown("""---""") 


    st.markdown("###### 잔차분석 - DecisionTreeRegressor 모델") 
    img4 = Image.open('graph_04.png')
    st.image(img4)
    st.markdown(r"""
	- residuals(잔차)는 zero
	- predicted value(예측값)은 0.76 ~ 2.6 사이인데....  그 의미는?
    """)
    st.markdown("""---""") 

    st.markdown("###### 학습곡선 - DecisionTreeRegressor 모델") 
    img5 = Image.open('graph_05.png')
    st.image(img5)
    st.markdown(r"""
	- cross validation score가 드디어 보입니다. (데이터 복사전에는 보이지 않았습니다.)
	- training instances 120 dlgn score 1.0이 됩니다.
		* 120번 훈련에서 1.0점을 달성하고 / 총 300번 이상 훈련한 것으로 해석됩니다.
    """)
    st.markdown("""---""") 


    st.markdown("###### feature importance plot") 
    img6 = Image.open('graph_06.png')
    st.image(img6)
    st.markdown(r"""
	- 2023년도 서울시 아파트 실거래가는
		* 과거 시세(2018년도) 아파트 실거래가의 경우 가장 높게 나타났습니다.    /  (데이터 복사전에는 2019년도)
		* 과거 시세(2022년도) 실거래가의 경우 높게 나타났습니다. / (데이터 복사전에는 (2020년도, 2021년도)
	- 데이터 복사 전과 데이터 복사 후의 feature importance 결과가 다르게 나왔습니다.
		* 이유는 ?
    """)
    st.markdown("""---""") 

with tabs[6]:
    st.markdown("####  3가지 가설에 대해 아래의 결과를 확인하였습니다.")
    st.markdown("""---""")

    st.markdown("######  1. 직전 5개년간 `서울시 구별 평균 개별공시지가 순위`는 차이는 없었습니다.")
    st.markdown(r"""
    """)
    st.markdown("""---""")

    st.markdown("######  2. 직전 6개년간 `서울시 구별 평균 아파트 실거래가의 순위`는 일부 차이가 있었습니다.")
    st.markdown(r"""
    """)
    st.markdown("""---""")

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

with tabs[7]:
    st.markdown(r"""
	- 자료 1. 매년 토지소재지 자치구청장이 개별공시지가
		* http://data.seoul.go.kr/dataList/OA-1180/F/1/datasetView.do
	- 자료 2. 국토교통부 제공 아파트 실거래가 자료 
		* http://rtdown.molit.go.kr
	- 자료 3. 서울시 소재 병원은 881개가 있습니다.
		* https://data.seoul.go.kr/dataList/OA-16479/S/1/datasetView.do
	- 자료 4. 서울시 소재 학교는 총 3,932개가 있습니다. 
		* https://data.seoul.go.kr/dataList/199/S/2/datasetView.do
	- 자료 5. 서울시 소재 도서관은 총 537개 가 있습니다. 
		* https://data.seoul.go.kr/dataList/387/S/2/datasetView.do
	- 자료 6. 서울시 소재 지하철역은 총 288개 가 있습니다. 
		* https://www.data.go.kr/data/15081868/fileData.do
	- 자료 7. 서울시 소재 버스정류장은 총 430개 가 있습니다. 
		* https://data.seoul.go.kr/dataList/OA-21225/S/1/datasetView.do
    """)
    st.markdown("""---""") 

