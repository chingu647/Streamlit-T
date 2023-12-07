def run_tab():
    st.markdown("###### 가설3 : `서울시 구별 평균 아파트 실거래가'는 서울시 구별 인프라 수준과 관계가 있다 ?") 


    st.markdown("###### 회귀모델별 비교") 
    img3 = Image.open('./imgs/graph_03.png')
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
    img4 = Image.open('./imgs/graph_04.png')
    st.image(img4)
    st.markdown(r"""
	- residuals(잔차)는 zero
	- predicted value(예측값)은 0.76 ~ 2.6 사이인데....  그 의미는?
    """)
    st.markdown("""---""") 

    st.markdown("###### 학습곡선 - DecisionTreeRegressor 모델") 
    img5 = Image.open('./imgs/graph_05.png')
    st.image(img5)
    st.markdown(r"""
	- cross validation score가 드디어 보입니다. (데이터 복사전에는 보이지 않았습니다.)
	- training instances 120 dlgn score 1.0이 됩니다.
		* 120번 훈련에서 1.0점을 달성하고 / 총 300번 이상 훈련한 것으로 해석됩니다.
    """)
    st.markdown("""---""") 


    st.markdown("###### feature importance plot") 
    img6 = Image.open('./imgs/graph_06.png')
    st.image(img6)
    st.markdown(r"""
	- 2023년도 서울시 아파트 실거래가는
		* 과거 시세(2018년도) 아파트 실거래가의 경우 가장 높게 나타났습니다.    /  (데이터 복사전에는 2019년도)
		* 과거 시세(2022년도) 실거래가의 경우 높게 나타났습니다. / (데이터 복사전에는 (2020년도, 2021년도)
	- 데이터 복사 전과 데이터 복사 후의 feature importance 결과가 다르게 나왔습니다.
		* 이유는 ?
    """)
    st.markdown("""---""") 
