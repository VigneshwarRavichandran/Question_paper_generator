from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
  data = request.get_json()
  total_marks = data['marks']
  n_easy_questions = data['easy']
  n_medium_questions = data['medium']
  n_hard_questions = data['hard']
  marks = (n_easy_questions*5) + (n_medium_questions*10) + (n_hard_questions*15)
  if marks != total_marks:
    return jsonify({
        'message' : 'Inappropriate number of questions'
      })
  questions = [
    {
      'question' : 'What is Python? What are the benefits of using Python?',
      'difficulty' : 'easy',
      'marks' : 5
    },
    {
      'question' : 'What is pickling and unpickling?',
      'difficulty' : 'easy',
      'marks' : 5

    },
    {
      'question' : 'How Python is interpreted?',
      'difficulty' : 'easy',
      'marks' : 5
    },
    {
      'question' : 'How memory is managed in Python?',
      'difficulty' : 'medium',
      'marks' : 10
    },
    {
      'question' : 'What are the tools that help to find bugs or perform static analysis?',
      'difficulty' : 'easy',
      'marks' : 5
    },
    {
      'question' : 'What are Python decorators?',
      'difficulty' : 'hard',
      'marks' : 15
    },
    {
      'question' : 'What is the difference between list and tuple?',
      'difficulty' : 'medium',
      'marks' : 10
    },
    {
      'question' : 'How are arguments passed by value or by reference?',
      'difficulty' : 'hard',
      'marks' : 15
    },
    {
      'question' : 'What is Dict and List comprehensions are?',
      'difficulty' : 'easy',
      'marks' : 5
    },
    {
      'question' : 'What are the built-in type does python provides?',
      'difficulty' : 'medium',
      'marks' : 10
    },
    {
      'question' : 'What is lambda in Python?',
      'difficulty' : 'easy',
      'marks' : 5
    },
    {
      'question' : 'Why lambda forms in python does not have statements?',
      'difficulty' : 'easy',
      'marks' : 5
    },
    {
      'question' : 'What is pass in Python?',
      'difficulty' : 'easy',
      'marks' : 5
    },
    {
      'question' : 'In Python what are iterators?',
      'difficulty' : 'medium',
      'marks' : 10
    },
    {
      'question' : 'What is unittest in Python?',
      'difficulty' : 'easy',
      'marks' : 5
    },
    {
      'question' : 'In Python what is slicing?',
      'difficulty' : 'hard',
      'marks' : 15
    },
    {
      'question' : 'What is docstring in Python?',
      'difficulty' : 'medium',
      'marks' : 10
    },
    {
      'question' : 'What is negative index in Python?',
      'difficulty' : 'hard',
      'marks' : 15
    },
    {
      'question' : 'How you can convert a number to a string?',
      'difficulty' : 'easy',
      'marks' : 5
    },
    {
      'question' : 'Mention the use of // operator in Python?',
      'difficulty' : 'medium',
      'marks' : 10
    }
  ]
  easy_questions = []
  medium_questions = []
  hard_questions = []
  for question in questions:
    if question['difficulty'] == 'easy':
      easy_questions.append(question['question'])
    elif question['difficulty'] == 'medium':
      medium_questions.append(question['question'])
    else:
      hard_questions.append(question['question'])
  questions = random.sample(easy_questions, n_easy_questions) + random.sample(medium_questions, n_medium_questions) + random.sample(hard_questions, n_hard_questions)
  return jsonify({
    "question" : questions
  })

if __name__ == '__main__':
  app.run(debug=True)