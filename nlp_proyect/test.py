
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