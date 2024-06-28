import pandas as pd

class dataFrame:
    def __init__(self,data = ""):
        self.data = data
        self.df = ""
        self.exceptionList = []

    def initDataFrame(self,columnList):
        self.df = pd.DataFrame(columns=columnList)
        return self
    
    def makeCRUDMatrixInMssql(self):
        # 데이터프레임 행 삽입
        for i in range(len(self.data)):
            # print(self.data[i])
            if self.data[i] == "INSERT":
                table_name = self.data[i + 2]
                if self.data[i - 1] != "THEN":  # MERGE일 경우 방지
                    if table_name in self.df['tableName'].values:
                        self.df.loc[self.df['tableName'] == table_name, 'Create'] = '○'
                    else:
                        self.df = self.df._append(
                            {'tableName': table_name, 'Create': '○', 'Read': "", 'Update': "", 'Delete': ""},
                            ignore_index=True)
            if self.data[i] == "FROM":
                table_name = self.data[i + 1]
                if (table_name != 'SELECT'):  # 서브쿼리를 SELECT하는 경우 방지
                    if table_name in self.df['tableName'].values:
                        self.df.loc[self.df['tableName'] == table_name, 'Read'] = '○'
                    else:
                        self.df = self.df._append(
                            {'tableName': table_name, 'Create': "", 'Read': '○', 'Update': "", 'Delete': ""},
                            ignore_index=True)
            if self.data[i] == "UPDATE":
                table_name = self.data[i + 1]
                if table_name == 'SET':
                    table_name = self.data[i + 2]
                if table_name in self.df['tableName'].values:
                    self.df.loc[self.df['tableName'] == table_name, 'Update'] = '○'
                else:
                    self.df = self.df._append({'tableName': table_name, 'Create': "", 'Read': "", 'Update': '○', 'Delete': ""},
                                    ignore_index=True)
            if self.data[i] == "JOIN":
                table_name = self.data[i + 1]
                if (table_name != '('):
                    if table_name in self.df['tableName'].values:
                        self.df.loc[self.df['tableName'] == table_name, 'Read'] = '○'
                    else:
                        self.df = self.df._append(
                            {'tableName': table_name, 'Create': "", 'Read': '○', 'Update': "", 'Delete': ""},
                            ignore_index=True)
            if self.data[i] == "DELETE":
                table_name = self.data[i + 1]
                if (table_name == 'FROM'):
                    table_name = self.data[i + 2]
                if table_name in self.df['tableName'].values:
                    self.df.loc[self.df['tableName'] == table_name, 'Delete'] = '○'
                else:
                    self.df = self.df._append({'tableName': table_name, 'Create': "", 'Read': "", 'Update': "", 'Delete': '○'},
                                    ignore_index=True)
            if self.data[i] == "MERGE":
                table_name = self.data[i + 1]
                if table_name in self.df['tableName'].values:
                    self.df.loc[self.df['tableName'] == table_name, 'INSERT'] = '○'
                    self.df.loc[self.df['tableName'] == table_name, 'UPDATE'] = '○'
                else:
                    self.df = self.df._append({'tableName': table_name, 'Create': '○', 'Read': "", 'Update': '○', 'Delete': ""},
                                    ignore_index=True)
            if(self.data[i]) == "WITH":
                table_name = self.data[i + 1]
                self.exceptionList.append(table_name) #합성 테이블은 예외목록에 넣는다

        for excepion in self.exceptionList: #예외목록 데이터프레임에서 삭제
            #self.df.drop(excepion,'rows')
            pass

        # 중복된 테이블명에 대해 값 병합
        self.df = self.df.groupby('tableName', as_index=False).agg({
            'Create': 'max',
            'Read': 'max',
            'Update': 'max',
            'Delete': 'max'
        })
        return self

    def getDataFrame(self):
        return self.df

    def getDataFrameToCsv(self):
        return self.df.to_csv(sep='\t', index=False)