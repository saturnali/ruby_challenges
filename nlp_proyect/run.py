
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