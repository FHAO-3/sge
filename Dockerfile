FROM python:3.13-slim

# "WORKDIR" onde vai ser execultado os comando que sao passados no final do arquivo
# WORKDIR <nome-projeto>
WORKDIR /sge

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN python manage.py migrate

# "EXPOSE" expoem uma porta
# EXPOSE <port>
EXPOSE 8000

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000