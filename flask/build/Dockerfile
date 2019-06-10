FROM python:3.6-slim

ADD requirements.txt /
RUN pip3 install -r requirements.txt

ADD api.py /
ADD sk.pkl /

EXPOSE 5000
ENTRYPOINT ["python", "api.py"]