import streamlit as st
import joblib
import numpy as np

def run_ml():
    st.subheader('ML: 비만정도 예측 인공지능')
    st.info('아래에 생활습관을 체크하여 비만정도를 예측하세요.')
    # 예측하기위해서 필요한 파일들을 불러와야 한다.
    # 인공지능파일과 스케일러 파일 2개


    regressor = joblib.load('data/regressor_obs.pkl')
    scaler_X = joblib.load('data/scaler_X_obs.pkl')
    scaler_y = joblib.load('data/scaler_y_obs.pkl')
    ct = joblib.load('data/ct_obs.pkl')


# 사용자가 데이터 입력

# 가족력(체질), 고칼로리음식을 좋아하고 자주먹는지, 하루에 몇끼마다 야채를 먹는지, 식사 외 음식섭취 얼마나 하는지  {no,Sometimes,Frequently,Always}
# 담배하는지, 물 몇컵 먹는지, 하루에 운동 몇번 하는지, 스마트 기기 하루에 몇시간, 술 얼마나 마시는지
    frequency = ['전혀','가끔','자주','항상']
    frequency_eng = ['no','Sometimes','Frequently','Always']  
    y_or_n = ['예','아니요']

    FH = st.radio('가족중에 살이 잘 찌는 체질이 있습니까?', y_or_n)
    if FH == y_or_n[0]:
        FH = 1
    else:
        FH = 0
    st.write("""***""")

    FAVC = st.radio('고칼로리 음식을 좋아하고 자주 먹습니까?', y_or_n)
    if FAVC == y_or_n[0]:
        FAVC = 1
    else:
        FAVC = 0
    st.write("""***""")

    FCVC  = st.radio('야채를 얼마나 자주 먹습니까? (절임류 제외)', frequency)
    if FCVC  == frequency[0]:
        FCVC  = 0
    elif FCVC  == frequency[1]:
        FCVC  = 1
    elif FCVC  == frequency[2]:
        FCVC  = 2
    else:
        FCVC  = 3
    st.write("""***""")

    CAEC  = st.radio('식사 외에 음식을 얼마나 자주 드십니까?', frequency) #인코딩
    if CAEC  == frequency[0]:
        CAEC  = frequency_eng[0]
    elif CAEC  == frequency[1]:
        CAEC  = frequency_eng[1]
    elif CAEC  == frequency[2]:
        CAEC  = frequency_eng[2]
    else:
        CAEC  = frequency_eng[3]
    st.write("""***""")

    SMOKE = st.radio('흡연을 하십니까?', y_or_n)
    if SMOKE == y_or_n[0]:
        SMOKE = 1
    else:
        SMOKE = 0
    st.write("""***""")

    CH2O  = st.radio('물을 하루에 얼마나 마십니까?', ['전혀 안마시는 날도 있다','1~2잔','3~5잔','6잔 이상'])
    if CH2O  == '전혀 안마시는 날도 있다':
        CH2O  = 0
    elif CH2O  == '1~2잔':
        CH2O  = 1
    elif CH2O  == '3~5잔':
        CH2O  = 2
    else:
        CH2O  = 3
    st.write("""***""")

    FAF  = st.radio('하루에 얼마나 자주 몸을 움직이십니까?', frequency)
    if FAF  == frequency[0]:
        FAF  = 0
    elif FAF  == frequency[1]:
        FAF  = 1
    elif FAF  == frequency[2]:
        FAF  = 2
    else:
        FAF  = 3
    st.write("""***""")

    TUE  = st.radio('하루에 스마트기기를 얼마나 자주 사용하십니까?', ['거의 사용하지 않는다','보통','하루종일'])
    if TUE  == '거의 사용하지 않는다':
        TUE  = 0
    elif TUE  == '보통':
        TUE  = 1
    else:
        TUE  = 2
    st.write("""***""")

    CALC  = st.radio('술을 얼마나 마십니까?', frequency) #인코딩
    if CALC  == frequency[0]:
        CALC  = frequency_eng[0]
    elif CALC  == frequency[1]:
        CALC  = frequency_eng[1]
    elif CALC  == frequency[2]:
        CALC  = frequency_eng[2]
    else:
        CALC  = frequency_eng[3]
    st.text('')

    if st.button('비만정도 예측'): 

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


        url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTExMTJfNDAg%2FMDAxNTczNTM5MDIxMTYz.umA_hxqnSsdsYfQSIGL4Icr00er_1BU1enplZ0lISyog.TsSFrf_crxobhTQ_6Y_hDNlg2at17bqpsfrcM4rahAUg.PNG.rainbi92%2Fimage.png&type=sc960_832'
        if y_pred[0,0] < 23:
            st.success('일반적인 사람들의 습관을 갖고있으며 정상적인 범주에 있습니다.\n\n현재의 건강한 습관을 유지하세요.\n\n해당 습관을 가진 사람들의 평균 BMI는 '+ str(round(y_pred[0,0],1)) +' 입니다.')
        elif y_pred[0,0] >= 23 and y_pred[0,0] < 30:
            st.warning('비만인 사람들의 습관을 갖고있습니다.\n\n나쁜 습관을 버리고 건강한 습관을 가지세요.\n\n해당 습관을 가진 사람들의 평균 BMI는 '+ str(round(y_pred[0,0],1)) +' 입니다.')
        elif y_pred[0,0] >= 30:
            st.error('비만인 사람들의 습관을 많이 갖고있으며 성인병을 주의해야 합니다.\n\n나쁜 습관을 버리고 건강한 습관을 가지세요.\n\n해당 습관을 가진 사람들의 평균 BMI는 '+ str(round(y_pred[0,0],1)) +' 입니다.')
        st.image(url,use_column_width=True)