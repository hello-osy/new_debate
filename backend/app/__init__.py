from flask import Flask
from flask_socketio import SocketIO

# Flask와 Socket.IO 초기화
socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)

    # Blueprint 등록
    from .routes import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    # Socket.IO 이벤트 등록
    from .socket_events import register_socket_events
    register_socket_events(socketio)

    socketio.init_app(app)
    return app
