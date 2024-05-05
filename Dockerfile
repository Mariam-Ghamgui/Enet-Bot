FROM rasa/rasa:3.6.16-full

WORKDIR /app

COPY . /app

USER root

RUN rasa train

VOLUME /app/models

CMD ["run", "-m", "/app/models", "--enable-api", "--cors", "*", "--debug", "--endpoints", "endpoints.yml", "--log-file", "out.log"]

EXPOSE 5005
