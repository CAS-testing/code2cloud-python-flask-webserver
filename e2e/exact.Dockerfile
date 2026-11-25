FROM python:3.10-slim
WORKDIR /srv/r2-exact
ENV E2E_CASE=bce63729-r2-exact
RUN mkdir -p /srv/r2-exact/www && echo "bce63729 r2 exact" > /srv/r2-exact/www/index.html
RUN useradd -u 10010 r2user
USER r2user
EXPOSE 5000
CMD ["python", "-m", "http.server", "5000", "--directory", "/srv/r2-exact/www"]
