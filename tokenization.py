from transformers import AutoTokenizer
from config import MODEL_NAME

def count_tokens(text: str, model=MODEL_NAME):
    tokenizer = AutoTokenizer.from_pretrained(model)
    return len(tokenizer.encode(text))
