from fileManager import fileManager,selectFile
from textProcessor import textProcessor
from dataFrame import dataFrame

if __name__ == '__main__':
    print('Jungducking')
    #기본 환경값 세팅(GUI 호출)
    filePath = selectFile()
    # 데이터 불러오기
    fm = fileManager(filePath)
    str = fm.readTextFile()

    #텍스트 전처리 파이프라인
    tp = textProcessor(str)
    resultStr = (tp
                    .upper()            #모두 대문자 변환
                    .removeAnnotation() #주석 제거
                    .removeEscapeChar() #개행문자 제거
                    .removeTabChar()    #탭 제거
                    .removeBraket()     #괄호 제거
                    .splitSpace()       #공백문자를 기준으로 리스트 생성
                    .removeEmptyEle()   #빈 요소 제거
                    .getResultList()    #리스트 반환
                 )

    #데이터프레임 생성
    df = dataFrame(resultStr)
    df.initDataFrame(['tableName','Create','Read','Update','Delete']) #데이터프레임 컬럼 지정 생성
    df.makeCRUDMatrixInMssql()
    print(df.getDataFrame()) #데이터 프레임 출력

    #print(df.getDataFrameToCsv()) #데이터 프레임 csv형식(탭 문자로 구분)으로 출력



