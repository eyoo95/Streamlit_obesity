import streamlit as st
import joblib
import numpy as np

def run_ml():
    st.subheader('ML: 비만정도 예측 인공지능')
    st.info('아래에 생활습관을 입력하여 비만정도를 예측하세요.')
    # 예측하기위해서 필요한 파일들을 불러와야 한다.
    # 인공지능파일과 스케일러 파일 2개


    regressor = joblib.load('data/regressor_obs.pkl')
    scaler_X = joblib.load('data/scaler_X_obs.pkl')
    scaler_y = joblib.load('data/scaler_y_obs.pkl')
    ct = joblib.load('data/ct_obs.pkl')


# 사용자가 데이터 입력

# 성별, 나이, 가족력(체질), 고칼로리음식을 좋아하고 자주먹는지, 하루에 몇끼마다 야채를 먹는지, 하루 몇끼먹는지, 식사 외 음식섭취 얼마나 하는지  {no,Sometimes,Frequently,Always}
# 담배하는지, 물 몇컵 먹는지, 매 끼니마다 칼로리를 재고 먹는지, 하루에 운동 몇번 하는지, 스마트 기기 하루에 몇시간, 술 얼마나 마시는지, 운송수단

    gender = st.radio('성별을 고르세요', ['남자','여자'])
    if gender == '여자':
        gender = 0
    else:
        gender = 1

    age = st.number_input('나이를 입력하세요(만 나이)',0,100,25)
    FH = st.radio('가족중에 살이 잘 찌는 체질이 있습니까?', ['예','아니요'])
    if FH == '아니요':
        FH = 0
    else:
        FH = 1
    FAVC = st.radio('고칼로리 음식을 좋아하고 자주 먹습니까?', ['예','아니요'])
    if FAVC == '아니요':
        FAVC = 0
    else:
        FAVC = 1
    FCVC = st.number_input('하루에 몇끼마다 야채를 먹습니까?',0,20)
    NCP = st.number_input('하루 식사를 몇번 하십니까?',0,10)
    CAEC  = st.radio('식사 외에 음식을 얼마나 자주 드십니까?', ['전혀','가끔','자주','항상'])
    if CAEC  == '전혀':
        CAEC  = 'no'
    elif CAEC  == '가끔':
        CAEC  = 'Sometimes'
    elif CAEC  == '자주':
        CAEC  = 'Frequently'
    else:
        CAEC  = 'Always'
    SMOKE = st.radio('흡연을 하십니까?', ['예','아니요'])
    if SMOKE == '아니요':
        SMOKE = 0
    else:
        SMOKE = 1
    CH2O  = st.number_input('물을 하루에 몇컵 마십니까?',0,10)    


    if st.button('비만정도 예측'): 


        # 1. 신규고객의 정보를 넘파이 어레이로 만들어준다.
        new_data = np.array([[windspeed, temperature, precipitation, humidity]])

        # 2. CT로 인코딩 하고 학습할때 사용한 X의 피텨스케일링을 이용해서 피처스케일링 한다.
        new_data = ct.transform(new_data)
        new_data = scaler_X.transform(new_data)

        # 3. 인공지능에게 예측해달라고 한다.
        new_pred = regressor.predict(new_data)

        # new_pred = new_pred.reshape(1,1)

        # 4. 예측한값을 원상복구한다.
        y_pred = scaler_y.inverse_transform(new_pred)

        # st.error('해당지역의 사고율은 '+ str(round(y_pred[0,0])) +'% 입니다.')
        # st.text("'교통사고는 기상상황 외에 수많은 요인들이 있기 때문에 극적인 사고율 변화는 없습니다.'")

