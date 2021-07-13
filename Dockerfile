FROM python:3.9

ADD . .

RUN pip install --upgrade pip
RUN pip install numpy


CMD ["python", "-m", "unittest", "discover", "-s","./Tests"]