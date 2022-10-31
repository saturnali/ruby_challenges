
from datasets import load_dataset
from transformers import AutoTokenizer
from transformers import DefaultDataCollator
import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification
from matplotlib import pyplot as plt

class model_trainer():
    def __init__(self, samples_data_test, samples_data_train):

      #samples of dataset
      self.samples_data_train = samples_data_train
      self.samples_data_test = samples_data_test

      #Loading dataset
      self.emotions = load_dataset("emotion")

      #Data collator
      self.data_collator = DefaultDataCollator(return_tensors="tf")

      self.BATCH_SIZE = 8

    def tokenize(self,rows):
      return self.tokenizer(rows['text'], padding="max_length", truncation=True)
