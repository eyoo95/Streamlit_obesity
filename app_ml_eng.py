import streamlit as st
import joblib
import numpy as np
from PIL import Image

def run_ml_eng():
    st.subheader('ML: you can predict your obesity level.')
    st.info('Please check the list for your life style information and predict your obesity level.')
    # 예측하기위해서 필요한 파일들을 불러와야 한다.
    # 인공지능파일과 스케일러 파일 2개


    regressor = joblib.load('data/regressor_obs.pkl')
    scaler_X = joblib.load('data/scaler_X_obs.pkl')
    scaler_y = joblib.load('data/scaler_y_obs.pkl')
    ct = joblib.load('data/ct_obs.pkl')


# 사용자가 데이터 입력

# 가족력(체질), 고칼로리음식을 좋아하고 자주먹는지, 하루에 몇끼마다 야채를 먹는지, 식사 외 음식섭취 얼마나 하는지  {no,Sometimes,Frequently,Always}
# 담배하는지, 물 몇컵 먹는지, 하루에 운동 몇번 하는지, 스마트 기기 하루에 몇시간, 술 얼마나 마시는지
    frequency_eng = ['no','Sometimes','Frequently','Always']  
    y_or_n = ['Yes','No']

    FH = st.radio('Family history with overweight', y_or_n)
    if FH == y_or_n[0]:
        FH = 1
    else:
        FH = 0
    st.write("""***""")

    FAVC = st.radio('Frequent consumption of high caloric food', y_or_n)
    if FAVC == y_or_n[0]:
        FAVC = 1
    else:
        FAVC = 0
    st.write("""***""")

    FCVC  = st.radio('Frequency of consumption of vegetables', frequency_eng)
    if FCVC  == frequency_eng[0]:
        FCVC  = 0
    elif FCVC  == frequency_eng[1]:
        FCVC  = 1
    elif FCVC  == frequency_eng[2]:
        FCVC  = 2
    else:
        FCVC  = 3
    st.write("""***""")

    CAEC  = st.radio('Consumption of food between meals', frequency_eng) #인코딩
    st.write("""***""")

    SMOKE = st.radio('Do you smoke?', y_or_n)
    if SMOKE == y_or_n[0]:
        SMOKE = 1
    else:
        SMOKE = 0
    st.write("""***""")

    CH2O  = st.radio('Consumption of water daily', frequency_eng)
    if CH2O  == frequency_eng[0]:
        CH2O  = 0
    elif CH2O  == frequency_eng[1]:
        CH2O  = 1
    elif CH2O  == frequency_eng[2]:
        CH2O  = 2
    else:
        CH2O  = 3
    st.write("""***""")

    FAF  = st.radio('Physical activity frequency', frequency_eng)
    if FAF  == frequency_eng[0]:
        FAF  = 0
    elif FAF  == frequency_eng[1]:
        FAF  = 1
    elif FAF  == frequency_eng[2]:
        FAF  = 2
    else:
        FAF  = 3
    st.write("""***""")

    TUE  = st.radio('Time using technology devices', ['Never','Usually','addicted'])
    if TUE  == 'Never':
        TUE  = 0
    elif TUE  == 'Usually':
        TUE  = 1
    else:
        TUE  = 2
    st.write("""***""")

    CALC  = st.radio('Consumption of alcohol', frequency_eng) #인코딩
    st.text('')


    if st.button('Show obesity level'): 

        # 1. 사용자의 정보를 넘파이 어레이로 만들어준다.
        new_data = np.array([[FH, FAVC, FCVC, CAEC, SMOKE, CH2O, FAF, TUE, CALC]])

        # 2. CT로 인코딩 하고 학습할때 사용한 X의 피텨스케일링을 이용해서 피처스케일링 한다.
        new_data = ct.transform(new_data)
        new_data = scaler_X.transform(new_data)

        # 3. 인공지능에게 예측해달라고 한다.
        new_pred = regressor.predict(new_data)

        new_pred = new_pred.reshape(1,1)

        # 4. 예측한값을 원상복구한다.
        y_pred = scaler_y.inverse_transform(new_pred)

        
        img = Image.open('data/20180201213201_9513.jpg')
        if y_pred[0,0] < 23:
            st.success('You have a life style that a normal person has.\n\nKeep your healthy life style.\n\nThe average BMI with the life style you selected was '+ str(round(y_pred[0,0],1)) +'.')
            st.image(img,use_column_width=True)
        elif y_pred[0,0] >= 23 and y_pred[0,0] < 30:
            st.warning('You have a life style that an obese person has.\n\nYou need to get away from bad life style and have a healthy life style.\n\nThe average BMI with the life style you selected was '+ str(round(y_pred[0,0],1)) +'.')
            st.image(img,use_column_width=True)
        elif y_pred[0,0] >= 30:
            st.error('You have a life style that an obese person has.\n\nAnd you need to be alert to the adult disease.\n\nYou have to get away from bad life style and get a healthy life style.\n\nThe average BMI with the life style you selected was '+ str(round(y_pred[0,0],1)) +'.')
            st.image(img,use_column_width=True)