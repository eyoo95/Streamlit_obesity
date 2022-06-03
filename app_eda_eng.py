import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import plotly.express as px


def run_eda_eng():
    st.subheader('EDA: You can see the correlation coefficient between related columns you selected')

    ### 데이터프레임 가져오기###
    df = pd.read_csv('data/Obesity_Levels_&_Life_Style_eng.csv')

    # 유저가 선택한 컬럼들 상관계수를 보여준다.
    col_list = df.columns[2:]
    st.text('')
    selected_list = st.multiselect('Please select two or more columns',col_list)
    st.text('')
    df_choice = df[selected_list]
    radio_corr = ['pairplot','correlation chart','heatmap']
    if len(selected_list) > 1:
        select_corr = st.radio('Choose how to display the correlation coefficient',radio_corr)
        st.text('')
        st.text("Correlation coefficient of selected columns")

        if select_corr == radio_corr[0]:               
            fig = sb.pairplot(data = df[selected_list])
            st.pyplot(fig)

        if select_corr == radio_corr[1]:     
            st.dataframe(df_choice.corr())
        
        if select_corr == radio_corr[2]:  
            fig2 = plt.figure()
            sb.heatmap(data= df[selected_list].corr(),annot=True,fmt='.2f', vmin=-1, vmax=1, cmap='coolwarm',linewidths= 0.5)
            st.pyplot(fig2)
        
    st.text("*if you want to check the columns, visit 'Home'")
