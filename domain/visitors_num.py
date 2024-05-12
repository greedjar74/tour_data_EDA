import streamlit as st
import pandas as pd
import numpy as np
import os
import plotly.express as px

def visitors_num():
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

    key_nums = st.slider('지역 개수', 1, 5, 1, 1)
    key_tmp = st.text_input('지역을 입력하세요(띄어쓰기로 구분)')
    key_list = key_tmp.split(' ')

    st.write('지역: ')
    for key in key_list:
        st.write(key)

    selected_data_list = []
    for i in range(key_nums):
        tmp = pd.concat([data for data in data_list[key_list[i]]['방문자수']])
        tmp['지역'] = key_list[i]
        selected_data_list.append(tmp)

    all_data = pd.concat([region_data for region_data in selected_data_list]).reset_index(drop=True)
    st.write(all_data)
    fig = px.line(all_data, x='기준년월', y='방문자수', color='지역', symbol='지역', markers=True)
    st.write(fig)