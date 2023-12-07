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


main()


















if __name__ == '__main__': 
    main()

