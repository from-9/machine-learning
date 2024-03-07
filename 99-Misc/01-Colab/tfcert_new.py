import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

TF_VERSION = '2.13.0'


def run_test():
    print('[텐서플로우 인증시험 환경 테스트 시작]')
    xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
    ys = np.array([5.0, 6.0, 7.0, 8.0, 9.0, 10.0], dtype=float)

    model = Sequential([
        Dense(1, input_shape=[1])
    ])

    model.compile(optimizer="sgd", loss="mse")
    model.fit(xs, ys, epochs=1600, verbose=0)
    prediction = model.predict([10.0])[0][0]
    print('---'*20)
    print(f'설치된 텐서플로우 버전: {tf.__version__}')
    if not tf.__version__ == TF_VERSION:
        print('[텐서플로우 환경 테스트 실패]')
        print(f'[사유] 권장 설치버전은: {TF_VERSION} 버전입니다.')

    print(f'샘플데이터 예측값: {prediction:.6f}')
    err = abs(prediction - 16.000046)
    if err < 1e-5:
        print('[텐서플로우 환경 테스트 통과]')
    else:
        print('[텐서플로우 환경 테스트 실패]')
        
    print('[텐서플로우 인증시험 환경 테스트 종료]')
    print('---'*20)
    

if _name_ == '_main_':
    run_test()
