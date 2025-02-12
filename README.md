# new_debate

## 개발 기간

2025.02.12~

## 명령어

```
docker-compose down
docker-compose up -d --build
```

## 구조

```
┌─────────────────────────────────────────────────────────┐
│                  Docker Network (Bridge)                │
│                                                         │
│   ┌─────────────┐      ┌─────────────┐      ┌────────┐  │
│   │ Frontend    │ <--->│ Backend     │ <--->│ DB     │  │
│   │ (Vue.js)    │ API  │ (Flask)     │ SQL  │(MYSQL) │  │
│   └─────────────┘      └─────────────┘      └────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

- Frontend (Vue.js): 사용자 인터페이스(UI) 제공
- Backend (Flask + Socket.IO): API 및 비즈니스 로직 처리
- Database (MySQL): 데이터 저장 및 관리
- Docker Network: 컨테이너 간 통신을 위한 가상 네트워크

## 전체 요청 흐름

1. 프론트엔드(Vue.js)에서 http://localhost:5000/api/match 요청
2. 백엔드(Flask)에서 routes.py로 요청 전달
3. db.py에서 MySQL 연결 후 INSERT INTO matches 실행
4. 데이터가 db 컨테이너(MySQL)에 저장됨
5. 성공 응답을 프론트엔드로 반환
