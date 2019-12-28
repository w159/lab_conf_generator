FROM python

ADD lcg /lcg

COPY lcg_docker.py /
COPY requirements.txt /

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "lcg_docker.py"]

#CMD -h