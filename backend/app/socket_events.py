from flask_socketio import emit, join_room

# 대기열 및 방 정보 (routes.py와 공유)
waiting_users = []
rooms = {}

def register_socket_events(socketio):
    @socketio.on("connect")
    def handle_connect():
        print("🔗 사용자 연결됨")

    @socketio.on("disconnect")
    def handle_disconnect():
        print("❌ 사용자 연결 종료")

    @socketio.on("join")
    def handle_join(data):
        user_id = data.get("user_id")

        if waiting_users:
            partner_id = waiting_users.pop(0)
            room_id = f"room_{user_id}_{partner_id}"
            rooms[room_id] = [user_id, partner_id]

            join_room(room_id)
            emit("matched", {"room_id": room_id, "partner_id": partner_id}, to=user_id)
            emit("matched", {"room_id": room_id, "partner_id": user_id}, to=partner_id)
        else:
            waiting_users.append(user_id)
