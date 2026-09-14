import pymysql
import config

conn = pymysql.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    db=config.DB_NAME,
    charset="utf8mb4"
)
cur = conn.cursor()

cur.execute("delete from memo where id = %s", (1,))

conn.commit()
print("삭제 완료")

conn.close()
