import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import plotly.express as px

############### 그래프에서 한국어 인식 ###############
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Linux':
    rc('font', family='NanumGothic')    
else:
    print('Unknown system')
############### 그래프에서 한국어 인식 ###############

def run_eda():
    st.subheader('EDA: 데이터 분석')
    st.info('대사증후군 통계와 생활습관 통계를 분석할수 있습니다.')

    df = pd.read_csv('data/Obesity_2018_2020.csv',index_col=0)
    # 라디오 버튼을 이용하여 데이터프레임과 통계치를 선택래서 볼수있게 한다.
    if st.checkbox('데이터프레임 생성'):
        st.text('')

        radio_menu = ['데이터프레임','통계치']
        selected = st.radio('보고 싶은 데이터프레임을 선택하세요.', radio_menu)

        if selected == radio_menu[0]:
            data_topic = ['전체','비만유병률 ','대사증후군 발병현황','가공식품 섭취빈도','휴가 사용유무','스마트기기 사용시간','대사증후군 위험요인']
            selected_data = st.selectbox('보고싶은 데이터프레임을 고르세요.',data_topic)

            #전체
            if selected_data == data_topic[0]:
                st.dataframe(df.sort_values(['년도','나이대'],axis=0))

            #비만유병률
            elif selected_data == data_topic[1]:
                st.text('비만유병률은 체질량지수(bmi)가 25kg/㎡ 이상인 분율입니다.')
                st.dataframe(df.iloc[:,:3].sort_values(['년도','나이대'],axis=0))
                if st.checkbox('차트 생성'):
                    fig = px.line(df, x="년도", y="비만유병률", color='나이대')
                    st.plotly_chart(fig)

            #대사증후군 발병현황
            elif selected_data == data_topic[2]:
                st.dataframe(df.iloc[:,:5].sort_values(['년도','나이대'],axis=0))
            
            #가공식품 섭취빈도
            elif selected_data == data_topic[3]:  # 설문형 결과
                st.dataframe(df.iloc[:,[0,1,2,5,6,7,8,9,10]].sort_values(['년도','나이대'],axis=0))
            
            #휴가 사용유무
            elif selected_data == data_topic[4]:
                st.dataframe(df.iloc[:,[0,1,2,11,12]].sort_values(['년도','나이대'],axis=0))
            
            #스마트기기 사용시간
            elif selected_data == data_topic[5]:  # 설문형 결과
                st.dataframe(df.iloc[:,[0,1,2,13,14,15,16,17]].sort_values(['년도','나이대'],axis=0))

            #대사증후군 위험요인
            else:
                st.dataframe(df.iloc[:,[0,1,2,18,19,20,21,22]].sort_values(['년도','나이대'],axis=0))

        if selected == radio_menu[1]:
            st.dataframe(df.describe())

    
