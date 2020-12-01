FROM python:3.6.1
EXPOSE 5000
WORKDIR /project
ADD . /project
RUN pip3 install -r requirements.txt
CMD python app.py