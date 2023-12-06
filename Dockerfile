FROM python:3.10

COPY . .
RUN git pull origin main
RUN pip install poetry==1.7.1
RUN poetry install --no-cache
ENTRYPOINT ["poetry", "run", "python", "main.py"]
