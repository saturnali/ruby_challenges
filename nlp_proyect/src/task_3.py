
from google.cloud import translate_v2
import requests, uuid
from nltk.translate.bleu_score import sentence_bleu
import statistics
import os

class translate_blue():
  def __init__(self, lang1_set, lang2_set, lang_from, lang_to, key_azure, region_azure, gcp_keys_json_name):