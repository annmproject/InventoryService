FROM python:3.8-slim
WORKDIR /app
COPY ./api/main.py /app/main.py
RUN pip install Flask
EXPOSE 80
CMD ["python", "main.py"]