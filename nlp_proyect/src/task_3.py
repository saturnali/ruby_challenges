
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

    headers = {
        'Ocp-Apim-Subscription-Key': self.cod_key,
        # location required if you're using a multi-service or regional (not global) resource.
        'Ocp-Apim-Subscription-Region': self.cod_region,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # You can pass more than one object in body.
    body = [{
        'text': text
    }]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return response[0]["translations"][0]["text"]

  def gcp_translate(self,text):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.gcp_keys_json_name
    client = translate_v2.Client()
    output = client.translate(text, self.lang_to)
    return output['translatedText']

  def main(self):
    points_gcp = []
    points_azure = []
    with open(self.lang1, 'r') as f:
      lang1 = f.readlines()

    with open(self.lang2, 'r') as f:
      lang2 = f.readlines()

    for i in range(len(lang1)):
      output_azure = self.azure_translate(lang1[i])
      #print(output_azure)