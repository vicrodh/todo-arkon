FROM node:17.6.0-alpine
WORKDIR /app/frontend
COPY project/package.json project/yarn.lock project/yarn.lock ./
COPY . ./
RUN yarn install
CMD ["yarn", "run", "build", "start"]
EXPOSE 3000
