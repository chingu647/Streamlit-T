#!pip install streamlit_jupyter

"""라이브러리 설치"""

import streamlit as st
from streamlit_jupyter import StreamlitPatcher, tqdm
StreamlitPatcher().jupyter()

# 기본 12종
import pandas as pd
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.patches import Patch

import seaborn as sns
import re
import time
import os

from datetime import datetime
from collections import Counter

"""## **1. streamlit-jupyter 예시 따라하기**"""

def main():
    st.title("서울시 아파트 가격 추세분석 및 예측")
    name = '장인구'
    st.text(f"제 이름은 {name}입니다.")
    st.header(f"이 영역은 헤더")
    st.subheader(f"이 영역은 서브헤더")

    st.title("EXAMPLE")
    st.markdown("#큰 글자")
main()

def main2():
    name = st.text_input("이름은?", "john")

    date = st.date_input("날짜는?", datetime.now())

    st.markdown(f"## 안녕하세요 {name}님 !!!")
    st.markdown(f"## 날짜는 {date.strftime('%Y-%m-%d')}입니다!!!")


main2()

date = datetime.now().strftime('%Y-%m-%d')

def main3():
  def get_data(date):
    for i in tqdm(range(50)):
      time.sleep(0.1)

    return pd.DataFrame(np.random.randint(1,10,(5,4)),
                        index=pd.date_range(date,periods=5),
                        columns=list('ABCD') )
  df = get_data(date)
  st.write(df)

main3()

import plotly.express as px

def main4():
  df = pd.DataFrame(np.random.randint(1,10,(5,4)),
                    index=pd.date_range(date,periods=5),
                    columns=list('ABCD') )
  fig = px.line(df,
                title='plotly.express graph',
                y=df.A,
                width=600)
  st.write(fig)
main4()

def main5():
  rd_option = st.radio('Choose on radio option', options=['foo','bar'])
  sb_option = st.selectbox('Select box', options=['Jane','Bob','Alice'], index=0)
  ms_options = st.multiselect('Multiselect', options=['python','golang','julia'])
  ms_options2 = st.multiselect('Multiselect', options=['python','golang','julia'], default=['python','julia'])
main5()

def main6():
  st.metric("Speed", 300, 210)

main6()


