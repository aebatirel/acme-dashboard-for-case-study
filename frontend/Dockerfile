FROM node:16

WORKDIR /app

COPY package*.json ./
COPY . .

RUN npm install

RUN npm run build

RUN npm install -g http-server

CMD ["http-server", "dist"]
