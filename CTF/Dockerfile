# syntax=docker/dockerfile:1

FROM node:22-alpine AS builder
RUN apk add --no-cache tzdata
RUN echo "web-0x00-user:x:1000:1000::/home/web-0x00-user:/usr/sbin/nologin" > /etc/passwd && \
    echo "web-0x00-group:x:1000:" > /etc/group
WORKDIR /dependencies
COPY package*.json ./
RUN npm ci --production

FROM node:22-alpine AS development-runner
WORKDIR /app
RUN npm i -g nodemon
COPY --from=builder /dependencies/node_modules ./node_modules
COPY ./src ./src
ENTRYPOINT [ "nodemon", "src/server.js" ]

FROM scratch AS production-runner
WORKDIR /app
COPY --from=node:22-alpine /usr/local/bin/node /usr/local/bin/node
COPY --from=node:22-alpine /lib /lib
COPY --from=node:22-alpine /usr/lib /usr/lib
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo
COPY --from=builder /dependencies/node_modules ./node_modules
COPY ./src ./src
USER web-0x00-user
ENTRYPOINT [ "/usr/local/bin/node", "src/server.js" ]