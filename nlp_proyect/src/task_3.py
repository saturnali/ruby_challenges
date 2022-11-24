
from google.cloud import translate_v2
import requests, uuid
from nltk.translate.bleu_score import sentence_bleu
import statistics
import os