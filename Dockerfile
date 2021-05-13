FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app/
#COPY . /usr/app/
COPY main.py  /app/
COPY requirements.txt .
COPY random_forest_classifier_model.pkl .
#EXPOSE 5000
#WORKDIR /usr/app/
RUN pip install -r requirements.txt
CMD ["python", "main.py"]