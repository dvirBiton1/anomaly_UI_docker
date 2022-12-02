FROM python:3.10
WORKDIR /app
COPY requirments.txt ./requirments.txt
RUN pip install -r requirments.txt
EXPOSE 8501
COPY . /app
ENTRYPOINT ["streamlit", "run"]

CMD ["anomaly_UI.py"]