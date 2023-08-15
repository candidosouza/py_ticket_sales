FROM python:3.11

RUN apt update && apt install -y --no-install-recommends curl wget
RUN  python -m pip install --upgrade pip

RUN useradd -ms /bin/bash python

RUN pip install poetry

USER python

WORKDIR /home/python/app

ENV PYTHONPATH=${PYTHONPATH}/home/python/app
ENV PATH="$PATH:/home/python/.local/bin"


CMD ["tail", "-f", "/dev/null"]