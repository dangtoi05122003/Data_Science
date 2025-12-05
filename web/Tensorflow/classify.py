import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences
from Tensorflow.model_builder import build_model

class TensorFlowClassifier:
    def __init__(self, models ="../models/Tensorflow/models_1.weights.h5", tokenizer= "../models/Tensorflow/tokenizers.pkl", label_encoder="../models/Tensorflow/label_encoder.pkl",max_len=100, vocab_size=10000):
        self.tokenizer = pickle.load(open(tokenizer, "rb"))
        self.label_encoder = pickle.load(open(label_encoder, "rb"))
        num_classes = len(self.label_encoder.classes_)
        self.max_len = max_len
        self.model = build_model(vocab_size=vocab_size, num_classes=num_classes, max_len=max_len)
        self.model.build(input_shape=(None, max_len))
        self.model.load_weights(models)

    def predict(self, processed_text):
        if not processed_text.strip():
            return {"label": "", "prob": 0.0}

        seq = self.tokenizer.texts_to_sequences([processed_text])
        padded = pad_sequences(seq, maxlen=self.max_len, padding="post", truncating="post")
        prediction = self.model.predict(padded)[0]
        label_index = prediction.argmax()
        label_name = self.label_encoder.inverse_transform([label_index])[0]
        prob = prediction.max()
        return {"label": label_name, "prob": prob}
