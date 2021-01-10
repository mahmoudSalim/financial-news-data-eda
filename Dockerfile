FROM python:3.6

ADD requirements /sentiment-analyzer/requirements

WORKDIR /sentiment-analyzer/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . .

EXPOSE 8081

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8081"]
