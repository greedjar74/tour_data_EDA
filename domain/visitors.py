import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px

from statsmodels.tsa.seasonal import seasonal_decompose

def visitors():
    data_path = '/Users/kimhongseok/eda_side_project/tour_data_EDA/data/한국관광 데이터랩/방문자수추이'
    region_list = os.listdir(data_path)
    region_list.sort()
    region_list.pop(0)

    data_list = dict()
    for region in region_list:
        data_list[region] = {'방문자수':[], '거주지':[], '성연령':[]}
        
    data_list['전국'] = {'방문자수':[]}

    for region in region_list:
        region_path_list = os.listdir(data_path+f'/{region}')
        region_path_list.sort()
        region_path_list.pop(0)
        if region == '전국':
            for path in region_path_list:
                df_tmp = pd.read_csv(data_path+f'/{region}/{path}', encoding='cp949')
                data_list[region]['방문자수'].append(df_tmp)
        else :    
            for i in range(15):
                path = region_path_list[i]
                df_tmp = pd.read_csv(data_path+f'/{region}/{path}', encoding='cp949')

                if i % 3 == 0:
                    data_list[region]['방문자수'].append(df_tmp)
                elif i % 3 == 1:
                    data_list[region]['거주지'].append(df_tmp)
                else :
                    data_list[region]['성연령'].append(df_tmp)

    # feature 통일 : 기준연월 -> 기준년월
    for data in data_list['전국']['방문자수']:
        data.columns = ['기준년월', '방문자수', '전년동기 방문자수', '방문자수 증감률', '관광지출액', '전년동기 관광지출액',
        '관광지출액 증감률']
        
    # datetime 형태로 변환
    for region in region_list:
        region_data_list = data_list[region]['방문자수']
        
        for data in region_data_list:
            region_date = data['기준년월'].tolist()
            new_region_date = list()
            
            for i in range(len(region_date)):
                tmp = f'{region_date[i]//100}.{region_date[i]%100}'
                new_region_date.append(tmp)
                
            data['기준년월'] = pd.DataFrame(new_region_date)
            data['기준년월'] = pd.to_datetime(data['기준년월'])

    # 전국은 단위가 10000명이므로 10000을 곱해준다.
    for data in data_list['전국']['방문자수']:
        data['방문자수'] = data['방문자수'] * 10000

    st.write('##### 지역:')
    st.write('전국, 서울, 경기도, 경상남도, 경상북도, 광주, 대구, 대전, 부산, 강원')
    st.write('세종, 울산, 인천, 전라남도, 전라북도, 제주, 충청남도, 충청북도')
    st.write('')
    key_tmp = st.text_input('지역을 입력하세요(띄어쓰기로 구분)')
    
    if len(key_tmp) != 0:
        key_list = key_tmp.split(' ')
        for key in key_list:
            st.write('##### 지역:',key)
            tmp = pd.concat([data for data in data_list[key]['방문자수']]).reset_index(drop=True)
            st.write(tmp)
            fig = px.line(tmp, x='기준년월', y='방문자수', markers=True)
            st.write(fig)

            # 데이터 세팅
            # 인덱스로 '기준연도' 설정, 빈도 일별('M')로 설정
            ts_data = tmp.set_index('기준년월').resample('M').mean().interpolate()

            # 시계열 분해 수행
            # 데이터를 트렌드, 계절성, 잔차로 분해
            decomposition = seasonal_decompose(ts_data['방문자수'], model='additive')
            fig_trend = px.line(decomposition.trend)
            fig_seasonal = px.line(decomposition.seasonal)
            st.write(fig_trend)
            st.write(fig_seasonal)
        
        if len(key_list) > 1:
            st.write('데이터 비교')
            selected_data_list = []
            for i in range(len(key_list)):
                tmp = pd.concat([data for data in data_list[key_list[i]]['방문자수']])
                tmp['지역'] = key_list[i]
                selected_data_list.append(tmp)

            all_data = pd.concat([region_data for region_data in selected_data_list]).reset_index(drop=True)
            st.write(all_data)
            fig = px.line(all_data, x='기준년월', y='방문자수', color='지역', symbol='지역', markers=True)
            st.write(fig)