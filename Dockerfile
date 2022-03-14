FROM python:2.7.18

ADD ./ /MidProject

WORKDIR /MidProject

RUN pip install -r requirements.txt

CMD ["uvicorn","main.py"]