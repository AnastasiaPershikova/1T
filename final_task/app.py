import pandas as pd
def employees_stat():
    data = pd.read_csv('data.csv', sep =';')
    print(f"Средняя зарплата сотрудников: {data['salary'].mean()}")
    print('Cотрудники старше 30 лет:')
    print(data[data['age']>30])
if __name__ == "__main__":
    employees_stat()