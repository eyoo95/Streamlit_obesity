import streamlit as st
import joblib
import numpy as np

def run_ml():
    st.subheader('ML: 사고율 예측 인공지능')
    st.info('아래에 기상정보를 입력하여 사고율을 예측하세요.')
    # 예측하기위해서 필요한 파일들을 불러와야 한다.
    # 인공지능파일과 스케일러 파일 2개


#     regressor = joblib.load('data/regressor_car.pkl')
#     scaler_X = joblib.load('data/scaler_X_car.pkl')
#     scaler_y = joblib.load('data/scaler_y_car.pkl')


# # 사용자가 데이터 입력

# # 풍속, 기온 , 강수량, 습도

#     windspeed = st.number_input('풍속을 입력하세요(m/s)',0,120)
#     temperature = st.number_input('온도를 입력하세요(℃)',-30,70)
#     precipitation = st.number_input('강수량을 입력하세요(mm)',0,3000)
#     humidity = st.number_input('습도를 입력하세요(%)',0,100)

#     if st.button('사고율 예측'): 


#         # 1. 신규고객의 정보를 넘파이 어레이로 만들어준다.
#         new_data = np.array([windspeed, temperature, precipitation, humidity])

#         # 2. 학습할때 사용한 X의 피텨스케일링을 이용해서 피처스케일링 한다.
#         # 먼저 데이터를 2차원으로 만든다. 
#         new_data = new_data.reshape(1,4)
#         new_data = scaler_X.transform(new_data)

#         # 3. 인공지능에게 예측해달라고 한다.
#         new_pred = regressor.predict(new_data)

#         new_pred = new_pred.reshape(1,1)

#         # 4. 예측한값을 원상복구한다.
#         y_pred = scaler_y.inverse_transform(new_pred)

#         st.error('해당지역의 사고율은 '+ str(round(y_pred[0,0])) +'% 입니다.')
#         st.text("'교통사고는 기상상황 외에 수많은 요인들이 있기 때문에 극적인 사고율 변화는 없습니다.'")

