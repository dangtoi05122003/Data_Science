import fasttext

class FastTextClassifier:
    def __init__(self, model_path = "../models/Fasttext/model.bin"):
        self.model = fasttext.load_model(model_path)

    def predict(self, processed_text):
        if not processed_text.strip():
            return {"topic": "", "subtopic": "", "prob": 0.0}
        
        labels, probs = self.model.predict(processed_text)
        label = labels[0].replace("__label__", "")
        prob = probs[0]
        parts = label.split("__")
        topic = parts[0]
        subtopic = parts[1] if len(parts) > 1 else ""
        return {"topic": topic, "subtopic": subtopic, "prob": prob}

