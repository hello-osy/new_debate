import os
import mysql.connector

def get_db_connection():
    """MySQL 데이터베이스 연결 생성"""
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "db"),   # Docker Compose에서 설정한 DB 컨테이너 이름
        user=os.getenv("MYSQL_USER", "user"),  # 환경 변수에서 가져오기
        password=os.getenv("MYSQL_PASSWORD", "password"),
        database=os.getenv("MYSQL_DB", "mydatabase")
    )
