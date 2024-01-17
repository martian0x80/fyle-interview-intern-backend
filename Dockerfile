FROM python:3.8

WORKDIR /app
COPY . /app

RUN pip install conda
RUN conda create -n env python=3.8
RUN conda activate env
RUN pip install -r requirements.txt

EXPOSE 7755

ENV FLASK_APP=core/server.py

CMD ["sh", "run.sh"]