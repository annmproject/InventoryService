FROM python:3.8-slim
WORKDIR /app
COPY ./api/main.py /app/main.py
EXPOSE 5555
RUN pip install Flask
RUN pip install flasgger
CMD ["python", "main.py"]