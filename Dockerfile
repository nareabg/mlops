# FROM python:3.8-slim

# WORKDIR /app

# COPY ./requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install connexion[swagger-ui]==2.14.2

# COPY . .

# EXPOSE 2000
# CMD ["python", "openapi_main.py"]

FROM python:3.8-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev

RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "app.py"]