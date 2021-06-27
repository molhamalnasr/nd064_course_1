FROM python:3.9
LABEL maintainer="Molham Al Nasr"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]