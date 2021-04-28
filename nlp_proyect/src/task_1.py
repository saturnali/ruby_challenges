#Import libraries
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

class movies_reviews():
    def __init__(self):
        #Preparing model and tokenizer
        self.model = AutoModelForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-sentiment")
        self.toke