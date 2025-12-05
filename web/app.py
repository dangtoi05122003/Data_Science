import streamlit as st
from Fasttext.classify import FastTextClassifier
from Tensorflow.classify import TensorFlowClassifier
from preprocessing import clean, stopword

@st.cache_resource
def load_fasttext():
    return FastTextClassifier()

@st.cache_resource
def load_tensorflow():
    return TensorFlowClassifier()

ft_model = load_fasttext()
tf_model =load_tensorflow()

st.title("Phân loại chủ đề")

tab1, tab2 = st.tabs(["FastText", "TensorFlow"])

with tab1:
    st.subheader("Dự đoán bằng FastText")
    text_ft = st.text_area("Nhập văn bản:", key="ft_text", height=150)
    if st.button("Dự đoán FastText"):
        if text_ft.strip():
            processed = stopword(clean(text_ft))
            result = ft_model.predict(processed)
            st.success(f"Topic: {result['topic']}")
            if result['subtopic']:
                st.info(f"Subtopic: {result['subtopic']}")
            st.caption(f"Xác suất dự đoán: {result['prob']:.2%}")
        else:
            st.warning("Vui lòng nhập văn bản")

with tab2:
    st.subheader("Dự đoán bằng TensorFlow")
    text_tf = st.text_area("Nhập văn bản:", key="tf_text", height=150)
    if st.button("Dự đoán TensorFlow"):
        if text_tf.strip():
            processed = stopword(clean(text_tf))
            result = tf_model.predict(processed)
            st.success(f"Nhãn dự đoán: {result['label']}")
            st.caption(f"Xác suất cao nhất: {result['prob']:.2%}")
        else:
            st.warning("Vui lòng nhập văn bản")

