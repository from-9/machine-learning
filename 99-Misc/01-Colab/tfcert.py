import subprocess

try:
    import google.colab
    IN_COLAB = True
except:
    IN_COLAB = False
    
if IN_COLAB:
    print('==='*20)
    print('설치환경: Google Colab')
    print('TensorFlow 시험환경을 구성중입니다. 잠시만 기다려 주세요.\n(설치는 약 1~5분 정도 소요 됩니다)')
    print('==='*20)
else:
    print('==='*20)
    print('설치환경: Local')
    print('TensorFlow 시험환경을 구성중입니다. 잠시만 기다려 주세요.\n(설치는 약 1~5분 정도 소요 됩니다)')
    print('==='*20)

subprocess.run(['pip', 'install', 'tensorflow==2.13.0'])
subprocess.run(['pip', 'install', 'tensorflow-datasets'])
subprocess.run(['pip', 'install', 'numpy'])
subprocess.run(['pip', 'install', 'Pillow'])
subprocess.run(['pip', 'install', 'scipy'])
subprocess.run(['pip', 'install', 'pandas'])
subprocess.run(['pip', 'install', 'urllib3'])
subprocess.run(['pip', 'install', 'protobuf'])

print('==='*20)
print('[알림] TensorFlow 시험환경 구성이 완료 되었습니다.')
print('==='*20)
    
