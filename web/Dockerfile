FROM node:lts-alpine3.18

WORKDIR /app

COPY package.json .
COPY . .

RUN npm install --omit=dev \
    && npm run generate

CMD npx --yes serve .output/public
