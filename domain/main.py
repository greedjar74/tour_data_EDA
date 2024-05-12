import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
from PIL import Image

from search_volume import search_volume
from visitors import visitors

def main_page():
    st.header('관광 데이터 분석')

def volume_EDA():
    st.write('## 관광지 검색량 분석')
    st.sidebar.write('관광지 검색량 데이터를 비교, 분석해보세요')
    search_volume()

def visitors_volume_EDA():
    st.write('## 지역 방문객수 분석')
    st.sidebar.write('지역 방문객수를 분석해보세요')
    visitors()

# 딕셔너리 선언 {  ‘selectbox항목’ : ‘페이지명’ …  }
page_names_to_funcs = {'Main Page': main_page, '관광지 검색량 분석': volume_EDA, '지역 방문객수 분석': visitors_volume_EDA}

# 사이드 바에서 selectbox 선언 & 선택 결과 저장
selected_page = st.sidebar.selectbox('Select a page', page_names_to_funcs.keys())

# 해당 페이지 부르기
page_names_to_funcs[selected_page]()