FROM python:3.11-alpine
WORKDIR /app
COPY requirements.txt pyproject.toml poetry.lock ./

RUN pip install --upgrade pip
RUN pip3 --no-cache-dir install -r requirements.txt
RUN poetry config virtualenvs.create false
RUN poetry install
ADD . /app/
