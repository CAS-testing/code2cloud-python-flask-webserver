FROM python:3.12-slim
WORKDIR /opt/prod
ENV E2E_CASE=e2e63731-prod
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /opt/prod/logs
COPY . .
EXPOSE 5002
CMD ["python", "index.py"]
