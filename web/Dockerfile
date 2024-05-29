FROM oven/bun:alpine

WORKDIR /app

COPY package.json .
COPY . .

RUN bun install --production && bun run generate

CMD bunx --yes serve .output/public
