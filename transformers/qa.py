from simpletransformers.question_answering import QuestionAnsweringModel
import json
import os

model = QuestionAnsweringModel('distilbert', 'distilbert-base-uncased-distilled-squad', args={'reprocess_input_data': True, 'overwrite_output_dir': True})

to_predict = [{'context': 'This is the context used for demonstrating predictions.', 'qas': [{'question': 'What is this context?', 'id': '0'}]}]

print(model.predict(to_predict))