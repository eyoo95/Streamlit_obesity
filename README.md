# 💉생활패턴으로 알아보는 비만정도 예측 앱

이 앱은 비만인 사람들의 습관을 학습하여 해당 습관들을 고르면 학습된 인공지능을 통하여 BMI를 예측하고 건강한 습관인지 잘못된 습관인지 알려주는 앱입니다.

사이드바에서 한국어와 영어를 고를수 있도록 했습니다.

# 메뉴구성
메뉴는 Home, EDA, ML로 구성되어 있습니다:

>Home: 이 앱의 사용목적과 사용된 데이터를 나타내었습니다.
>EDA: 사용된 데이터를 데이터프레임 등으로 나타내고 한눈에 보기쉽게 차트를 보여줍니다.
>ML: 학습된 인공지능을 바탕으로 사용자의 습관데이터를 수집하여 비만 정도를 예측합니다.

# 사용된 데이터
사용된 데이터는 두가지로 구분했습니다.
하나는 대한민국의 생활습관 및 질병통계 데이터입니다.
다른 하나는 남미에서 각 사람들의 생활습관과 몸무게, 키 등을 개별적으로 기록한 데이터입니다. 

대한민국에서 사용한 데이터는 모두 6개이며 조사군이 모두 달라서 인공지능을 학습시키기에는 적합하지 않다고 판단되어
인공지능을 학습시킬 데이터를 따로 구분하여 사용했습니다.

인공지능은 Random Forest를 사용했습니다.

*영어로 설정하면 대한민국 통계는 나타내지 않게 했습니다.

>주소
>http://52.79.80.210:8502/
