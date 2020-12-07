
from src.task_1 import movies_reviews
from src.task_2 import model_trainer
from src.task_3 import translate_blue


if __name__ == '__main__':
    print("Task 1: Out of the Box Sentiment Analysis ")
    task_1 = movies_reviews()
    task_1.main()
    print("-----------END------------")
    print("Task 2: Take a basic, pretrained NER model, and train further on a task-specific dataset")
    samples_train = 300
    samples_test = 30
    task_2 = model_trainer(samples_test, samples_train)
    task_2.main()
    task_2.graphic_model()
    print("-----------END------------")
    print("Task 3:Set up and compare model performance of two different translation models")
    lang1_set = 'nlp_proyect/en_corpus.txt'
    lang2_set = 'nlp_proyect/es_corpus.txt'
    lang_from = 'en'
    lang_to = 'es'
    cod_key = 'keyAzure'
    cod_region = 'zoneAzure'
    gcp_keys = 'nlp_proyect/private_key.json'