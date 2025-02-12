from flask import Blueprint, request, jsonify
from .db import get_db_connection  # ✅ db.py의 함수 가져오기

api_bp = Blueprint("api", __name__)

@api_bp.route("/match", methods=["POST"])
def match_user():
    data = request.json
    user_id = data.get("user_id")
    
    conn = get_db_connection() # 데이터베이스 연결
    cursor = conn.cursor() # 커서 생성

    # 사용자 매칭 정보 저장
    cursor.execute("INSERT INTO matches (user_id) VALUES (%s)", (user_id,)) # sql 쿼리 실행
    conn.commit() # 트랜잭션 커밋 (데이터 저장 확정)

    cursor.close() # 커서와 연결 종료
    conn.close()

    return jsonify({"status": "matched", "user_id": user_id})
