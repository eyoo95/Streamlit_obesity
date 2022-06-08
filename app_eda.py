import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
    st.info('대한민국의 대사증후군 통계와 생활습관 통계를 분석할수 있습니다.')

    ### csv 가져오기###
    df = pd.read_csv('data/Obesity_2018_2020.csv',index_col=0)
    df_disease = pd.read_csv('data/df_disease.csv',index_col=0)
    df_meta = pd.read_csv('data/df_meta.csv',encoding='cp949')
    df_processed_food = pd.read_csv('data/df_processed_food.csv',encoding='cp949')
    df_vacation = pd.read_csv('data/df_vacation.csv',encoding='cp949')
    df_smart = pd.read_csv('data/df_smart.csv',encoding='cp949')
    df_lifestyle = pd.read_csv('data/Obesity_Levels_&_Life_Style.csv',encoding='cp949')


    # 유저가 선택한 컬럼들 상관계수를 보여준다.
    col_list = df_lifestyle.columns[2:]

    if st.checkbox('학습데이터의 상관관계 확인'):
        st.text('')
        selected_list = st.multiselect('상관관계를 보기 원하면, 하나 이상의 컬럼을 선택하세요',col_list)
        st.text('')
        df_choice = df_lifestyle[selected_list]
        radio_corr = ['그래프','표','히트맵']
        if len(selected_list) > 1:
            select_corr = st.radio('상관계수를 표시할 방법을 선택하세요.',radio_corr)
            st.text('')
            st.text('선택한 컬럼들의 상관계수입니다.')

            if select_corr == radio_corr[0]:               
                fig = sb.pairplot(data = df_lifestyle[selected_list])
                st.pyplot(fig)

            if select_corr == radio_corr[1]:     
                st.dataframe(df_choice.corr())
            
            if select_corr == radio_corr[2]:  
                fig2 = plt.figure()
                sb.heatmap(data= df_lifestyle[selected_list].corr(),annot=True,fmt='.2f', vmin=-1, vmax=1, cmap='coolwarm',linewidths= 0.5)
                st.pyplot(fig2)

            st.warning('위쪽의 상관관계 확인 체크박스를 풀어서 상관관계 표를 해제할수 있습니다.')
            st.write("""***""")

    # 라디오 버튼을 이용하여 데이터프레임과 통계치를 선택해서 볼수있게 한다.
    if st.checkbox('데이터프레임 생성'):
        st.text('')

        radio_menu = ['데이터프레임','통계치']
        selected = st.radio('보고 싶은 데이터를 선택하세요.', radio_menu)

        if selected == radio_menu[0]:
            data_topic = ['전체','비만유병률 ','대사증후군 위험요인','대사증후군 발병현황','가공식품 섭취빈도','휴가 사용유무','스마트기기 사용시간']
            selected_data = st.selectbox('보고싶은 데이터프레임을 고르세요.',data_topic)

            age_list = ['전체 나이대','20대','30대','40대','50대','60대']
            get_age = st.selectbox('해당 나이대의 데이터를 검색합니다.',age_list) 
            if get_age == age_list[0]:
                get_age = '|'.join(age_list[1:])
            age_txt = get_age     
            if age_txt == '|'.join(age_list[1:]):
                age_txt = '전체 나이대'

            def year_separater(df,year,value,label):  # 파이 차트를 위한 2018, 2019, 2020 분리 함수
                v18 = df.loc[df[year]== 2018 ,][value].to_list()
                l18 = df.loc[df[year]== 2018 ,][label].to_list()
                v19 = df.loc[df[year]== 2019 ,][value].to_list()
                l19 = df.loc[df[year]== 2019 ,][label].to_list()
                v20 = df.loc[df[year]== 2020 ,][value].to_list()
                l20 = df.loc[df[year]== 2020 ,][label].to_list()
                return [v18,l18,v19,l19,v20,l20]

            #전체
            if selected_data == data_topic[0]:
                st.dataframe(df.loc[df['나이대'].str.contains(get_age),].sort_values(['년도','나이대'],axis=0))

            #비만유병률
            elif selected_data == data_topic[1]:
                
                st.dataframe(df.iloc[:,:3].loc[df['나이대'].str.contains(get_age),].sort_values(['년도','나이대'],axis=0))
                st.text('*비만유병률은 체질량지수(bmi)가 25kg/㎡ 이상인 사람들의 분율입니다.')
                if st.button('차트 생성'):
                    st.info('년도별, 나이대별로 비만유병률을 나타낸 차트입니다.')
                    fig = px.line(df, x="년도", y="비만유병률", color='나이대',markers=True)
                    st.plotly_chart(fig)

            #대사증후군 위험요인 (개별파일 필요)
            elif selected_data == data_topic[2]:
                df_disease_sel = df_disease.loc[df_disease['나이대'].str.contains(get_age),].sort_values(['년도','나이대'],axis=0)
                st.dataframe(df_disease_sel)
                if st.button('차트 생성'):
                    st.info('대사증후군을 앓고있는 사람중 관련 위험요인을 보유한 사람의 분율을 나타낸 차트입니다.')
                    fig = px.pie(df_disease_sel, values='명', names='유형',hole=.3)
                    st.plotly_chart(fig)

            #대사증후군 발병현황 (개별파일 필요)
            elif selected_data == data_topic[3]:
                df_meta_sel = df_meta.loc[df_meta['나이대'].str.contains(get_age),].sort_values(['년도','나이대'],axis=0)
                st.dataframe(df_meta_sel)
                if st.button('차트 생성'):
                    st.info('{}의 대사증후군 발병현황을 나타낸 차트입니다.'.format(age_txt))
                    meta_vl = year_separater(df_meta_sel,'년도','명','유형')
                    fig = make_subplots(1, 3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]],
                    subplot_titles=['2018', '2019','2020'])
                    fig.add_trace(go.Pie(values = meta_vl[0], labels = meta_vl[1], hole = 0.3,pull=[0.1,0,0]),1,1)
                    fig.add_trace(go.Pie(values = meta_vl[2], labels = meta_vl[3], hole = 0.3,pull=[0.1,0,0]),1,2)
                    fig.add_trace(go.Pie(values = meta_vl[4], labels = meta_vl[5], hole = 0.3,pull=[0.1,0,0]),1,3)
                    st.plotly_chart(fig)

            
            #가공식품 소비빈도 (개별파일 필요)
            elif selected_data == data_topic[4]:  # 설문형 결과
                df_processed_food_sel = df_processed_food.loc[df_processed_food['나이대'].str.contains(get_age),].sort_values(['년도','나이대'],axis=0)
                st.dataframe(df_processed_food_sel)
                if st.button('차트 생성'):
                    st.info('{}의 가공식품 소비빈도를 나타낸 차트입니다.'.format(age_txt))
                    pf_vl = year_separater(df_processed_food_sel,'년도','분율','유형')
                    fig = make_subplots(1, 3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]],
                    subplot_titles=['2018', '2019','2020'])
                    fig.add_trace(go.Pie(values = pf_vl[0], labels = pf_vl[1], hole = 0.3,pull=[0,0.1,0,0,0,0]),1,1)
                    fig.add_trace(go.Pie(values = pf_vl[2], labels = pf_vl[3], hole = 0.3,pull=[0,0.1,0,0,0,0]),1,2)
                    fig.add_trace(go.Pie(values = pf_vl[4], labels = pf_vl[5], hole = 0.3,pull=[0,0.1,0,0,0,0]),1,3)
                    st.plotly_chart(fig)
            
            #휴가 사용유무 (개별파일 필요)
            elif selected_data == data_topic[5]:
                df_vacation_sel = df_vacation.loc[df_vacation['나이대'].str.contains(get_age),].sort_values(['년도','나이대'],axis=0)
                st.dataframe(df_vacation_sel)
                if st.button('차트 생성'):
                    st.info('{}의 휴가 사용유무를 나타낸 차트입니다.'.format(age_txt))
                    pf_vc = year_separater(df_vacation_sel,'년도','분율','유형')
                    fig = make_subplots(1, 3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]],
                    subplot_titles=['2018', '2019','2020'])
                    fig.add_trace(go.Pie(values = pf_vc[0], labels = pf_vc[1], hole = 0.3,pull=[0,0.05]),1,1)
                    fig.add_trace(go.Pie(values = pf_vc[2], labels = pf_vc[3], hole = 0.3,pull=[0,0.05]),1,2)
                    fig.add_trace(go.Pie(values = pf_vc[4], labels = pf_vc[5], hole = 0.3,pull=[0,0.05]),1,3)
                    st.plotly_chart(fig)
            
            #스마트기기 사용시간  (개별파일 필요) # 설문형 결과
            elif selected_data == data_topic[6]:  
                df_smart_sel = df_smart.loc[df_smart['나이대'].str.contains(get_age),].sort_values(['년도','나이대'],axis=0)
                st.dataframe(df_smart_sel)
                if st.button('차트 생성'):
                    st.info('{}의 스마트기기 사용시간을 나타낸 차트입니다.'.format(age_txt))
                    pf_sm = year_separater(df_smart_sel,'년도','분율','유형')
                    fig = make_subplots(1, 3, specs=[[{'type':'domain'}, {'type':'domain'},{'type':'domain'}]],
                    subplot_titles=['2018', '2019','2020'])
                    fig.add_trace(go.Pie(values = pf_sm[0], labels = pf_sm[1], hole = 0.3,pull=[0,0,0.1,0.1,0.1]),1,1)
                    fig.add_trace(go.Pie(values = pf_sm[2], labels = pf_sm[3], hole = 0.3,pull=[0,0,0.1,0.1,0.1]),1,2)
                    fig.add_trace(go.Pie(values = pf_sm[4], labels = pf_sm[5], hole = 0.3,pull=[0,0,0.1,0.1,0.1]),1,3)
                    st.plotly_chart(fig)



        if selected == radio_menu[1]:
            st.dataframe(df.describe())