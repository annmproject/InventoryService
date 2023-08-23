FROM python:3.8-slim
WORKDIR /app
COPY ./api/main.py /app/main.py
RUN pip install Flask
CMD ["python", "main.py"]