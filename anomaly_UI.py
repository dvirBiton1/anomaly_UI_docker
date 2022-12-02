import pandas as pd
from sklearn.ensemble import IsolationForest
# from texttable import Texttable
import streamlit as st
import joblib
import time
from PIL import Image


# file path - this for linux windows you will need "//"
class docker_anomaly:
    def __init__(self, f_path):
        self.f_path = f_path
        self.model = IsolationForest(contamination="auto", n_estimators=1000)
        self.data = pd.read_csv(f_path, names=["record ID", "duration_", "src_bytes", "dst_bytes"], header=None)

    def create_model(self):
        self.model.fit(self.data)

    def predict(self, to_predict):
        self.new_model.fit(to_predict)
        an_or_na = self.new_model.predict(to_predict)
        if an_or_na == 1:
            print("not anomaly")
        else:
            print("anomaly")
        return an_or_na

    def save_model(self):
        ISModel = open("model/ISModel.pkl", "wb")
        joblib.dump(self.model, ISModel)
        ISModel.close()

    # def input_data(self):
    def load_model(self):
        model_f_path = open("model/ISModel.pkl", "rb")
        self.new_model = joblib.load(model_f_path)

    def load_css(self, file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

    def load_icon(self, icon_name):
        st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)

    def load_images(self, file_name):
        img = Image.open(file_name)
        return st.image(img, width=300)

    def main(self):
        """Anomaly Classifier App
          With Streamlit

        """

        st.title("Anomaly Classifier")
        html_temp = """
      """
        st.markdown(html_temp, unsafe_allow_html=True)
        self.load_model()
        record_id = st.number_input("Enter record id")
        duration = st.number_input("Enter duration")
        src_bytes = st.number_input("Enter src_bytes")
        dst_bytes = st.number_input("Enter dst_bytes")
        data = {"record ID": [record_id], "duration_": [duration], "src_bytes": [src_bytes],
                "dst_bytes": [dst_bytes]}
        test_anomaly = pd.DataFrame(data)
        if st.button("Predict"):
            result = self.predict(test_anomaly)
            if result[0] == 1:
                prediction = 'Not anomaly'
                img = 'zero.jpeg'
            else:
                prediction = 'anomaly'
                img = 'one.jpeg'

            st.success(
                f'record id: {record_id}, duration: {duration},src_bytes: {src_bytes}, dst_bytes:{dst_bytes} was classified as {prediction}')
            self.load_images(img)


if __name__ == '__main__':
    f_path = r"conn_attack.csv"
    '''
    record ID - The unique identifier for each connection record.
    duration_  This feature denotes the number of seconds (rounded) of the connection. For example, a connection for 0.17s or 0.3s would be indicated with a “0” in this field.
    src_bytes This field represents the number of data bytes transferred from the source to the destination (i.e., the amount of out-going bytes from the host).
    dst_bytes This fea
    ture represents the number of data bytes transferred from the destination to the source (i.e., the amount of bytes received by the host).
    '''
    # data = pd.read_csv(f_path, names=["record ID", "duration_", "src_bytes", "dst_bytes"], header=None)
    docker_anomaly_UI = docker_anomaly(f_path)
    # # docker_anomaly_UI.create_model()
    # # docker_anomaly_UI.save_model()
    docker_anomaly_UI.main()
