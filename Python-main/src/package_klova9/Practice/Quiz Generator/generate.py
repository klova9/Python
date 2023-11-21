import json
import random


with open('Python-main\src\package_klova9\Practice\Quiz Generator\questions.json') as f:
    quiz = json.dump(f)
print(random.choice(quiz['question']))
