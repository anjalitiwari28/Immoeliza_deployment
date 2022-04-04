FROM python:3.8 

WORKDIR /immoeliza_deployment

ADD ./requirements.txt .
RUN pip install -r requirements.txt

ADD . .

CMD ["python", "app.py"]

