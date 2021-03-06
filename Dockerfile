FROM python:3
ENV PYTHONUUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install pandas-datareader \
                django-extensions \
                Werkzeug \
                django-postgres-dropdb \
                djangorestframework \
                django-environ
COPY . /code/