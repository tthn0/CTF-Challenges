# syntax=docker/dockerfile:1

FROM python:3.13-alpine as builder
RUN echo "web-0x01-user:x:1000:1000::/home/web-0x01-user:/usr/sbin/nologin" > /etc/passwd && \
    echo "web-0x01-group:x:1000:" > /etc/group
WORKDIR /dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir --target=/dependencies -r requirements.txt

FROM python:3.13-alpine as development-runner
WORKDIR /app
COPY --from=builder /dependencies /usr/local/lib/python3.13/site-packages
COPY ./src ./src
ENTRYPOINT ["python", "src"]

FROM scratch as production-runner
WORKDIR /app
COPY --from=python:3.13-alpine /usr/local/lib /usr/local/lib
COPY --from=python:3.13-alpine /usr/local/bin /usr/local/bin
COPY --from=python:3.13-alpine /lib /lib
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /etc/group /etc/group
COPY --from=builder /usr/share/zoneinfo /usr/share/zoneinfo
COPY --from=builder /dependencies /usr/local/lib/python3.13/site-packages
COPY ./src ./src
USER web-0x01-user
ENTRYPOINT ["/usr/local/bin/python", "src"]