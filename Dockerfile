FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc wget texlive-full uwsgi-python3 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/app
RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"
ENV DEBIAN_FRONTEND=noninteractive

COPY . /usr/app
RUN pip install -r /usr/app/requirements.txt

RUN groupadd -g 1111 python && useradd -r -u 1111 -g python python
USER 1111

#CMD ["python", "wsgi.py"]
CMD [ "uwsgi", "--http", "0.0.0.0:5001", \
               "--uid", "uwsgi", \
               "--gevent", "100", \
               "--wsgi", "main:application" ]




