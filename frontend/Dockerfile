FROM node:16

WORKDIR /app

# package.json과 package-lock.json 파일 복사
COPY package*.json ./

# 필요한 패키지 설치 (socket.io-client 포함)
RUN npm install socket.io-client && npm install

COPY . .

EXPOSE 8080
CMD ["npm", "run", "serve"]
