import pymysql
import config


def get_connection():
    """데이터베이스 연결을 만들어 돌려줌 (5차시와 같은 코드)"""
    return pymysql.connect(
        host=config.DB_HOST,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        db=config.DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )


class LedDB:
    """LED 기록을 다루는 계층"""

    def add(self, pin, is_on):
        """켜고 끈 기록을 한 건 추가함"""
        conn = get_connection()

        try:
            with conn.cursor() as cursor:
                sql = """
                    INSERT INTO led_log (pin, is_on)
                    VALUES (%s, %s)
                """
                cursor.execute(sql, (pin, is_on))

            conn.commit()

        finally:
            conn.close()
