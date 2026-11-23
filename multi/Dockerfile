FROM python:3.11 AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip wheel --wheel-dir /wheels -r requirements.txt

FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*
ENV E2E_CASE=e2e63731-multi
RUN mkdir -p /app/data
COPY . /app
EXPOSE 5001
CMD ["python", "index.py"]
