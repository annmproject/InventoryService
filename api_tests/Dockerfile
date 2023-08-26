FROM python:3.8-slim
WORKDIR /app
COPY ./api_tests/integration_tests.py /app/integration_tests.py
RUN pip install requests
CMD ["python", "integration_tests.py"]