
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