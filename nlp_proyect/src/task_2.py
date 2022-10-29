
from datasets import load_dataset
from transformers import AutoTokenizer
from transformers import DefaultDataCollator
import tensorflow as tf
from transformers import TFAutoModelForSequenceClassification
from matplotlib import pyplot as plt

class model_trainer():