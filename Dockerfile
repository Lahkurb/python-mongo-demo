FROM alpine:latest

LABEL maintainer="James Anderton <janderton@burwood.com>"
LABEL description="MongoDB Python Demo App"

COPY ["requirements.txt", "."]

RUN apk --update add --no-cache python3 py3-pip \
&& pip3 install -U pip \
&& pip3 install -r requirements.txt \
&& pip3 list modules

ENV PORT 8080
EXPOSE 8080

WORKDIR /app
COPY ["src/", "/app/"]

ENTRYPOINT ["python3"]
CMD ["app.py"]

