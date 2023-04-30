FROM python:3.10

COPY . .

COPY ./requirements.txt .
COPY ./app .

RUN	python -m pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]