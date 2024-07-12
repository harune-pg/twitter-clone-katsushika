FROM node:lts-slim

WORKDIR /code
COPY package.json package.json
COPY package-lock.json package-lock.json

# package.jsonに基づいてパッケージをインストール
RUN npm install

COPY . .
