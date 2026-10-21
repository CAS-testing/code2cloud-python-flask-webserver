FROM python:3.10-bookworm

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get upgrade -y && apt-get clean

# Upgrade pip to latest version
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# Ensure SQLite is installed
RUN apt-get install -y sqlite3

# Install PHP 8.1 (Debian bookworm ships PHP 8.2 by default, so use the Sury PHP repository)
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl gnupg \
    && curl -sSLo /usr/share/keyrings/deb.sury.org-php.gpg https://packages.sury.org/php/apt.gpg \
    && echo "deb [signed-by=/usr/share/keyrings/deb.sury.org-php.gpg] https://packages.sury.org/php/ bookworm main" > /etc/apt/sources.list.d/php.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends php8.1-cli \
    && rm -rf /var/lib/apt/lists/* \
    && php -v

EXPOSE 5000

HEALTHCHECK CMD curl --fail http://localhost:5000 || exit 1   

CMD python ./index.py


