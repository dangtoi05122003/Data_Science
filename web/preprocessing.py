import re

def spam(text):
    if re.fullmatch(r"(\w+)\1{10,}", text):
        return ""
    if re.search(r"(.{2,10})\1{4,}", text):
        return ""
    tokens = text.split()
    if len(tokens) > 10 and len(set(tokens)) == 1:
        return ""
    return text

def clean(text):
    text = text.lower()
    http =re.sub(r"\b(?:https?|www|preview|redd|imgur|cdn)[^\s\"']+", " ", text)
    emoji = re.sub(r"[\U00010000-\U0010ffff]", " ", http)
    filter =re.sub(r"[^\w\sÀ-ỹ]", " ", emoji)
    remove_spam = spam(filter)
    data = re.sub(r"\s+", " ", remove_spam).strip()
    return data

def stopword(text, filepath="../Data/stopwords_vi.txt"):
    with open(filepath,'r', encoding='utf-8') as f:
        stopwords = set(f.read().splitlines())
    words = text.split()
    words = [w for w in words if w not in stopwords]
    return " ".join(words)