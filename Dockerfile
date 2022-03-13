FROM python:3.9.7

ADD ./ /MidProject

WORKDIR /MidProject

RUN pip install -r requirements.txt

CMD ["uvicorn","main.py"]