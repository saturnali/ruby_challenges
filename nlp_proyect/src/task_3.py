
from google.cloud import translate_v2
import requests, uuid
from nltk.translate.bleu_score import sentence_bleu
import statistics
import os

class translate_blue():
  def __init__(self, lang1_set, lang2_set, lang_from, lang_to, key_azure, region_azure, gcp_keys_json_name):
    self.lang1 = lang1_set
    self.lang2 = lang2_set
    self.lang_from = lang_from
    self.lang_to = lang_to
    self.cod_key = key_azure
    self.cod_region = region_azure
    self.gcp_keys_json_name = gcp_keys_json_name

  def azure_translate(self,text):
    # Add your key and endpoint
    endpoint = "https://api.cognitive.microsofttranslator.com"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': self.lang_from,
        'to': self.lang_to
    }
