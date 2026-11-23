FROM python:3.11-slim
WORKDIR /srv/api
COPY requirements.txt /srv/api/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN useradd -u 10001 apiuser
ENV E2E_CASE=e2e63731-svc-api
COPY . /srv/api
USER apiuser
EXPOSE 8080
CMD ["python", "main.py"]
