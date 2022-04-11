FROM node:17.6.0-alpine
ENV COMPOSE_HTTP_TIMEOUT=50000
ENV TERM="xterm-256color"
WORKDIR /app/frontend
COPY project/package.json project/package-lock.json ./
RUN npm install -g npm
RUN npm install
RUN npm install react-scripts -g && npm update
COPY . ./
EXPOSE 3000