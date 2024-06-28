2024.06.27

Made by Jungducking

CRUD 매트릭스를 보다 쉽게 작성하기 위한 툴입니다.

sqlMapper 파일을 읽어, 해당 파일 내에서 각 테이블들의 CRUD 현황을 조사하여 판다스 데이터프레임 또는 CSV 형식으로 출력합니다.

sqlMapper파일이 각 프로세스,화면 별 또는 엔티티 별로 작성되었을 경우에 더욱 도움이 될 것입니다.

240627 현재는 mssql의 문법만을 테스트 하였습니다. 다른 언어는 추후 추가할 예정입니다.

기능

파일을 GUI로 불러올 수 있도록 한다.
SELECT, INSERT, UPDATE, DELETE, MERGE, JOIN등의 키워드를 읽어 테이블의 CRUD 기능을 정의한다.
결과를 CSV로 출력할 수 있게 한다.
