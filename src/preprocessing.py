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
    data=[]
    with open(filepath,'r', encoding='utf-8') as f:
        stopword = f.read().splitlines()
    for i in text:
        if i is None:
            continue
        words = i.split()
        words = [w for w in words if w not in stopword]
        data.append(" ".join(words))
    return data