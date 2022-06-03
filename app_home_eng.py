import streamlit as st

def run_home_eng():
    st.subheader('Select the menu on the left')
    st.text('This app can predict the obesity level with your life style information')
    st.subheader("")
    st.info("Used data for this app:\n\nObesity Levels & Life Style")
    st.info("Column information:\n\nFAVC: Frequent consumption of high caloric food\n\nFCVC: Frequency of consumption of vegetables\n\nCAEC: Consumption of food between meals\n\nCH2O: Consumption of water daily\n\nFAF: Physical activity frequency\n\nTUE: Time using technology devices\n\nCALC: Consumption of alcohol")
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')


    st.text('Data from:\nhttps://www.kaggle.com/code/mpwolke/obesity-levels-life-style/data')

