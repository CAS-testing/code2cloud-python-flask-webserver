FROM python:3.10-slim
WORKDIR /srv/r2-delete
ENV E2E_CASE=bce63729-r2-delete
RUN mkdir -p /srv/r2-delete/www && echo "bce63729 r2 delete" > /srv/r2-delete/www/index.html
RUN useradd -u 10010 r2user
USER r2user
EXPOSE 5000
CMD ["python", "-m", "http.server", "5000", "--directory", "/srv/r2-delete/www"]
