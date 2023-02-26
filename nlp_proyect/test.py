
from src.task_1 import movies_reviews
from src.task_3 import translate_blue

import pytest


answer_task1 = ['Negative', 'Positive', 'Positive', 'Negative', 'Negative', 'Positive', 'Negative', 'Positive', 'Neutral', 'Positive', 'Positive', 'Positive', 'Neutral', 'Negative', 'Positive', 'Positive', 'Positive', 'Neutral', 'Positive', 'Negative']
def test_task1():
   #TEST TASK 1
    model = movies_reviews()
    list = model.main()
    assert list == answer_task1

def test_task3():
   #Test task 3
   lang1_set = 'nlp_proyect/en_corpus.txt'
   lang2_set = 'nlp_proyect/es_corpus.txt'
   lang_from = 'en'
   lang_to = 'es'
   cod_key = 'c72e1edd13a1410785bef1c40dd6224e'
   cod_region = 'southcentralus'
   gcp_keys = 'nlp_proyect/clave.json'
   model = translate_blue(lang1_set, lang2_set, lang_from, lang_to, cod_key, cod_region, gcp_keys)
   status = model.main()