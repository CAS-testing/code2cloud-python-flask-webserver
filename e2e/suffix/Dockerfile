FROM python:3.10-slim
WORKDIR /srv/r2-suffix
ENV E2E_CASE=bce63729-r2-suffix
RUN mkdir -p /srv/r2-suffix/www && echo "bce63729 r2 suffix" > /srv/r2-suffix/www/index.html
RUN useradd -u 10010 r2user
USER r2user
EXPOSE 5000
CMD ["python", "-m", "http.server", "5000", "--directory", "/srv/r2-suffix/www"]
