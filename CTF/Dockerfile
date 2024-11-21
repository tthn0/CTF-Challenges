# syntax=docker/dockerfile:1

FROM node:lts-alpine AS builder
WORKDIR /dependencies
COPY package*.json ./
RUN npm ci --production

FROM node:lts-alpine AS development-runner
WORKDIR /app
COPY --from=builder /dependencies/node_modules ./node_modules
RUN npm install -g nodemon && addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
ENTRYPOINT [ "nodemon", "src/server.js" ]

FROM node:lts-alpine AS production-runner
WORKDIR /app
COPY --from=builder /dependencies/node_modules ./node_modules
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
ENTRYPOINT [ "node", "src/server.js" ]
