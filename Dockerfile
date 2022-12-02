FROM python:3.10
WORKDIR /docker_Ex1
COPY requirements.txt ./requirements.txt
RUN pip install -r requiremts.txt
EXPOSE 8501
COPY ./app
ENTRYPOINT ["streamlit", "run"]

CMD ["anomaly_UI.py"]