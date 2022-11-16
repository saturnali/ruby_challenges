
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

    def split_dataset(self,data_set):
      self.small_train_dataset = data_set["train"].shuffle(seed=42).select([i for i in list(range(self.samples_data_train))])
      self.small_eval_dataset = data_set["test"].shuffle(seed=42).select([i for i in list(range(self.samples_data_test))])

    def tf_datasets(self):
      self.tf_train_dataset = self.small_train_dataset.to_tf_dataset(
          columns=["attention_mask", "input_ids"],
          label_cols=["labels"],
          shuffle=True,
          collate_fn=self.data_collator,
          BATCH_SIZE=self.BATCH_SIZE,
      )

      self.tf_validation_dataset = self.small_eval_dataset.to_tf_dataset(
          columns=["attention_mask", "input_ids"],
          label_cols=["labels"],
          shuffle=False,
          collate_fn=self.data_collator,
          BATCH_SIZE=self.BATCH_SIZE,
      )


    def train_model(self):
      self.model = TFAutoModelForSequenceClassification.from_pretrained(\
                                                                        "distilbert-base-uncased", num_labels=6)
      self.model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=5e-5),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=tf.metrics.SparseCategoricalAccuracy(),
        )

      self.history = self.model.fit(self.tf_train_dataset, validation_data=self.tf_validation_dataset,epochs=5)
      return self.model
      
    
    def main(self):
      self.model_ckpt = "distilbert-base-uncased"
      self.tokenizer = AutoTokenizer.from_pretrained(self.model_ckpt)
      self.emotions.set_format(type=None)
      self.tokenized_datasets = self.emotions.map(self.tokenize, batched=True)
      self.split_dataset(self.tokenized_datasets)
      self.tf_datasets()
      self.modelh = self.train_model()

    def graphic_model(self):
      plt.plot(self.history.history['loss'])
      plt.plot(self.history.history['val_loss'])
      plt.title('model loss')
      plt.ylabel('loss')
      plt.xlabel('epoch')
      plt.legend(['train', 'val'], loc='upper left')