FROM rasa/rasa-sdk:3.6.2

WORKDIR /app

COPY actions.py /app/actions.py
COPY requirements.txt /app/requirements.txt

USER root
RUN pip install -r requirements.txt

USER 1001

EXPOSE 5055
