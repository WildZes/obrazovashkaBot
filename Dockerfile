FROM python:3.6 AS builder
COPY requirements.txt

RUN pip install --user -r requirements.txt

FROM python:3.6-slim
WORKDIR /code

COPY --from=builder /root/.local/bin /root/.local
COPY obrazovashkaBot/ .

ENV PATH=/root/.local:$PATH

CMD [ "python", "./obrazovashka.py"]
