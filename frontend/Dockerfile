FROM node:17.6.0-alpine
ENV COMPOSE_HTTP_TIMEOUT=50000
ENV TERM="xterm-256color"
WORKDIR /app/frontend
COPY project/package.json project/package-lock.json project/tsconfig.json ./
RUN npm install -g npm
# RUN npm install && npm update && npm rebuild
RUN npm install react-scripts -g && npm update && npm rebuild
RUN npm i @emotion/react @emotion/styled && npm install @emotion/react --save
COPY ./project ./
EXPOSE 3000
