import pandas as pd
from sqlalchemy import create_engine

# Создаём класс для работы с БД
class DBWorker():
    # Подключение к БД
    # и получение данных 
    def get_db(self, dbname, user, password, query):
        #print('========INIT========')
        self.engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{server}/{dbname}').connect()
        self.df = pd.read_sql(query, con=self.engine)
        print(len(self.df))
        return self.df
        #print('========INIT END========')

    # переписываем даннык из DF
    # в масссив  
    def get_fild(self, df, N, fild: str):
        self.arr = list(range(0,N))
        for i in range(0, N):
            self.arr[i] = (df[fild].loc[df.index[i]])
        return self.arr

    # Отдельно для ФИО так как в БД другой формат записи
    # [Иванов Иван Иванович] --> [[Иванов],[Иван],[Иванович]] 
    def FIO(self, df, N):
        FIOarr = list(range(0, N))
        for i in range(0, N):
            FIOarr[i] = (df['name'].loc[df.index[i]])
        Splitarr = []
        i = 0
        while i <= N-1:
            Splitarr.append(str.split(FIOarr[i]))
            i = i + 1
        return Splitarr

# запрос к БД
query = """
    SELECT  field 
    FROM table 
    LEFT JOIN db.table
    ON tabel.field = db.table.field 
    INNER JOIN table
    ON table.field = table.field
    WHERE table.field = 'value'
    """

# Функция для формирования подключения и запроса от класса
def DBQuery(dbname):
    df = DBWorker.get_db(DBWorker, dbname, 'med', 'med', query)
    print(len(df))
    return df

# Обработка ответа БД
def DBRespons(df):    
    Name = DBWorker.FIO(DBWorker, df, len(df))
    Rvk = DBWorker.get_fild(DBWorker, df, len(df), 'rvk')
    Creator = DBWorker.get_fild(DBWorker, df, len(df), 'creatorID')
    Arrticl = DBWorker.get_fild(DBWorker, df, len(df), 'article')
    BirthDate = DBWorker.get_fild(DBWorker, df, len(df), 'birthDate')
    CreationDate = DBWorker.get_fild(DBWorker, df, len(df), 'creationDate')
    Diagnosis = DBWorker.get_fild(DBWorker, df, len(df), 'diagnosis')
    HealthCategory = DBWorker.get_fild(DBWorker, df, len(df), 'healthCategory')

    return df, Name, Rvk, Creator, Arrticl, BirthDate, CreationDate, Diagnosis, HealthCategory
