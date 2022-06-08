💉생활패턴으로 알아보는 비만정도 예측 앱
========

이 앱은 비만인 사람들의 습관을 학습하여 해당 습관들을 고르면
학습된 인공지능을 통하여 BMI를 예측하고 건강한 습관인지 잘못된 습관인지 알려주는 앱입니다.

사이드바에서 한국어와 영어를 고를수 있도록 했습니다.

메뉴구성
----
메뉴는 Home, EDA, ML로 구성되어 있습니다:

- Home: 이 앱의 사용목적과 사용된 데이터를 나타내었습니다.
- EDA: 사용된 데이터를 데이터프레임 등으로 나타내고 한눈에 보기쉽게 차트를 보여줍니다.
- ML: 학습된 인공지능을 바탕으로 사용자의 습관데이터를 수집하여 비만 정도를 예측합니다.

사용된 데이터
----
사용된 데이터는 두가지로 구분했습니다.
하나는 대한민국의 생활습관 및 질병통계 데이터입니다.
다른 하나는 남미에서 각 사람들의 생활습관과 몸무게, 키 등을 개별적으로 기록한 데이터입니다. 

Dataset:

KOSIS (대한민국 생활습관 및 질병통계)
- 비만 유병률(체질량지수 기준) 추이
- 연령별 성별 대사증후군 위험요인 보유개수별 현황
- 연령별 성별 대사증후군 위험요인별 현황
- 가공식품 구입 주기
- 지난 1년 동안) 휴가 경험 여부
- 스마트 기기 활용 시간_평일
>https://kosis.kr/statHtml/statHtml.do?orgId=177&tblId=DT_11702_N101&conn_path=I2


Kaggle (남미 비만과 생활습관 데이터)
- Obesity Levels & Life Style
>https://www.kaggle.com/code/mpwolke/obesity-levels-life-style/data

데이터 분리
----
대한민국에서 사용한 데이터는 모두 6개이며 조사군이 모두 달라서 인공지능을 학습시키기에는 적합하지 않다고 판단되어
인공지능을 학습시킬 데이터를 따로 구분하여 사용했습니다.

사용된 컬럼
----
대한민국 생활습관 및 질병통계
- 나이대: 나이대를 나타냅니다. 20대부터 60대까지 10대 간격으로 구성되어 있습니다.
- 년도: 년도를 나타냅니다. 2018년부터 2020년까지 있습니다.
- 비만유병률: 비만유병률을 나타냅니다. *비만유병률은 체질량지수(bmi)가 25kg/㎡ 이상인 사람들의 분율입니다.
- 복부비만: 건강진단 결과가 복부비만으로 나온 사람들의 수를 나타냅니다.
- 높은혈압: 건강진단 결과가 높은혈압으로 나온 사람들의 수를 나타냅니다.
- 높은혈당: 건강진단 결과가 높은혈당으로 나온 사람들의 수를 나타냅니다.
- 고중성지방혈증: 건강진단 결과가 고중성지방혈증으로 나온 사람들의 수를 나타냅니다.
- 낮은 HDL 콜레스테롤 혈증: 건강진단 결과가 낮은 HDL 콜레스테롤 혈증으로 나온 사람들의 수를 나타냅니다.
- 주의군: 대사증후군 위험요인이 1개 이상 3개 미만인 사람들의 수를 나타냅니다.
- 대사증후군: 대사증후군 위험요인이 3개 이상 6개 미만인 사람들의 수를 나타냅니다.
- 정상: 대사증후군 위험요인이 없는 사람들의 수를 나타냅니다.
- 매일소비: 가공식품을 매일소비한 사람 수의 나이대별 분율을 나타냅니다.
- 주 2~3회소비: 가공식품을 매일소비한 사람 수의 나이대별 분율을 나타냅니다.
- 주 1회소비: 가공식품을 주 1회 소비한 사람 수의 나이대별 분율을 나타냅니다.
- 2주 1회소비: 가공식품을 2주 1회 소비한 사람 수의 나이대별 분율을 나타냅니다.
- 월 1회소비: 가공식품을 월 1회 소비한 사람 수의 나이대별 분율을 나타냅니다.
- 월 1회 미만소비: 가공식품을 월 1회 미만 소비한 사람 수의 나이대별 분율을 나타냅니다.
- 휴가사용: 휴가를 사용한 사람 수의 나이대별 분율을 나타냅니다.
- 휴가미사용: 휴가를 사용하지 못한 사람 수의 나이대별 분율을 나타냅니다.
- 1시간 미만 사용: 스마트 기기를 1시간 미만 사용한 사람 수의 나이대별 분율을 나타냅니다.
- 1-2시간 사용: 스마트 기기를 1시간 이상 2시간 미만 사용한 사람 수의 나이대별 분율을 나타냅니다.
- 2-3시간 사용: 스마트 기기를 2시간 이상 3시간 미만 사용한 사람 수의 나이대별 분율을 나타냅니다.
- 3-4시간 사용: 스마트 기기를 3시간 이상 4시간 미만 사용한 사람 수의 나이대별 분율을 나타냅니다.
- 4시간 이상 사용: 스마트 기기를 4시간 이상 사용한 사람 수의 나이대별 분율을 나타냅니다.

남미 비만과 생활습관 데이터 (인공지능 학습에 사용)
- Family_history_with_overweight: 가족중에 과체중 혹은 비만인 사람이 있는지에 대한 여부를 나타냅니다.
- FAVC: 고칼로리 음식을 섭취하는 빈도를 나타냅니다.
- FCVC: 야채를 섭취하는 빈도를 나타냅니다.
- CAEC: 식사 외에 음식을 섭취하는 빈도를 나타냅니다.
- SMOKE: 흡연여부를 나타냅니다.
- CH2O: 수분을 섭취하는 빈도를 나타냅니다.
- FAF: 몸을 움직이는 빈도를 나타냅니다.
- TUE: 스마트기기를 사용하는 시간을 나타냅니다.
- CALC: 알콜을 섭취하는 빈도를 나타냅니다.
- BMI: 체질량지수를 나타냅니다.

사용된 라이브러리
----
- streamlit
>pip install streamlit
>
>streamlit hello
- streamlit_option_menu
>pip install streamlit_option_menu
- pandas
>pip install pandas
- seaborn
>pip install seaborn
- matplotlib.pyplot
> pip install matplotlib
- joblib
>pip install joblib
- numpy
>pip install numpy
-plotly
>pip install plotly

인공지능은 Random Forest를 사용했습니다.

----

*영어로 설정하면 대한민국 통계는 나타내지 않게 했습니다.


- 앱 주소: 
>http://ec2-52-79-80-210.ap-northeast-2.compute.amazonaws.com:8502/
