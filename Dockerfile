FROM python:3.6

RUN pip install --upgrade pip

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ADD app.py /

RUN pip install Flask==1.1.1

CMD [ "python", "app.py" ]