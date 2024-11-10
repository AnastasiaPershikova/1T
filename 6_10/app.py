import psycopg2
import os

def ages(db_name,db_user,db_password,db_host,db_port):
    conn = psycopg2.connect (
      database=db_name, 
      user=db_user, 
      password=db_password, 
      host=db_host, 
      port=db_port
    )
    with conn.cursor() as cur:
        sql =  """
    SELECT 
                                            min(age) AS min_age,
                                            max(age) AS max_age
                                        FROM test_table tt 
                                        WHERE length(name)<6"""
        cur.execute(sql)
        result = cur.fetchall()
        r =f'Минимальный возраст: {result[0][0]}, максимальны возраст: {result[0][1]}'
    conn.close
    return(r)

if __name__ == "__main__":
    db_name = os.environ.get("DB_NAME", "postgres")
    db_user = os.environ.get("DB_USER", "postgres")
    db_password = os.environ.get("DB_PASSWORD", "admin")
    db_host = os.environ.get("DB_HOST", "localhost")
    db_port = os.environ.get("DB_PORT", "5432")
    print(ages(db_name,db_user,db_password,db_host,db_port))
