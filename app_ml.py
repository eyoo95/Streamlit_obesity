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

    FCVC  = st.radio('야채를 얼마나 자주 먹습니까? (절임류 제외)', ['전혀','가끔','자주','항상'])
    if FCVC  == '전혀':
        FCVC  = 0
    elif FCVC  == '가끔':
        FCVC  = 1
    elif FCVC  == '자주':
        FCVC  = 2
    else:
        FCVC  = 3

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

    CH2O  = st.radio('물을 하루에 얼마나 마십니까?', ['전혀 안마시는 날도 있다','1~2잔','3~5잔','6잔 이상'])
    if CH2O  == '전혀 안마시는 날도 있다':
        CH2O  = 0
    elif CH2O  == '1~2잔':
        CH2O  = 1
    elif CH2O  == '3~5잔':
        CH2O  = 2
    else:
        CH2O  = 3

    FAF  = st.radio('하루에 얼마나 자주 몸을 움직이십니까?', ['거의 움직이지 않는다','가끔','자주','항상'])
    if FAF  == '거의 움직이지 않는다':
        FAF  = 0
    elif FAF  == '가끔':
        FAF  = 1
    elif FAF  == '자주':
        FAF  = 2
    else:
        FAF  = 3

    TUE  = st.radio('하루에 스마트기기를 얼마나 자주 사용하십니까?', ['거의 사용하지 않는다','보통','하루종일'])
    if TUE  == '거의 사용하지 않는다':
        TUE  = 0
    elif TUE  == '보통':
        TUE  = 1
    else:
        TUE  = 2

    CALC  = st.radio('술을 얼마나 마십니까?', ['전혀','가끔','자주','항상'])
    if CALC  == '전혀':
        CALC  = 'no'
    elif CALC  == '가끔':
        CALC  = 'Sometimes'
    elif CALC  == '자주':
        CALC  = 'Frequently'
    else:
        CALC  = 'Always'


    if st.button('비만정도 예측'): 


        # 1. 신규고객의 정보를 넘파이 어레이로 만들어준다.
        new_data = np.array([[FH, FAVC, FCVC, CAEC, SMOKE, CH2O, FAF, TUE, CALC]])

        # 2. CT로 인코딩 하고 학습할때 사용한 X의 피텨스케일링을 이용해서 피처스케일링 한다.
        new_data = ct.transform(new_data)
        new_data = scaler_X.transform(new_data)

        # 3. 인공지능에게 예측해달라고 한다.
        new_pred = regressor.predict(new_data)

        new_pred = new_pred.reshape(1,1)

        # 4. 예측한값을 원상복구한다.
        y_pred = scaler_y.inverse_transform(new_pred)

        if y_pred[0,0] < 23:
            st.success('일반적인 사람들의 습관을 갖고있으며 정상적인 범주에 있습니다.\n\n현재의 건강한 습관을 유지하세요.\n\n해당 습관을 가진 사람들의 평균 BMI는 '+ str(round(y_pred[0,0])) +' 입니다.')
            st.image('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTExMTJfNDAg%2FMDAxNTczNTM5MDIxMTYz.umA_hxqnSsdsYfQSIGL4Icr00er_1BU1enplZ0lISyog.TsSFrf_crxobhTQ_6Y_hDNlg2at17bqpsfrcM4rahAUg.PNG.rainbi92%2Fimage.png&type=sc960_832',use_column_width=True)
        elif y_pred[0,0] >= 23 and y_pred[0,0] < 30:
            st.warning('비만인 사람들의 습관을 갖고있습니다.\n\n나쁜 습관을 버리고 건강한 습관을 가지세요.\n\n해당 습관을 가진 사람들의 평균 BMI는 '+ str(round(y_pred[0,0])) +' 입니다.')
            st.image('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTExMTJfNDAg%2FMDAxNTczNTM5MDIxMTYz.umA_hxqnSsdsYfQSIGL4Icr00er_1BU1enplZ0lISyog.TsSFrf_crxobhTQ_6Y_hDNlg2at17bqpsfrcM4rahAUg.PNG.rainbi92%2Fimage.png&type=sc960_832',use_column_width=True)
        elif y_pred[0,0] >= 30:
            st.error('비만인 사람들의 습관을 많이 갖고있으며 성인병을 주의해야 합니다.\n\n나쁜 습관을 버리고 건강한 습관을 가지세요.\n\n해당 습관을 가진 사람들의 평균 BMI는 '+ str(round(y_pred[0,0])) +' 입니다.')
            st.image('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAxOTExMTJfNDAg%2FMDAxNTczNTM5MDIxMTYz.umA_hxqnSsdsYfQSIGL4Icr00er_1BU1enplZ0lISyog.TsSFrf_crxobhTQ_6Y_hDNlg2at17bqpsfrcM4rahAUg.PNG.rainbi92%2Fimage.png&type=sc960_832',use_column_width=True)