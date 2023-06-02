import  json

with open("questions.json",'r') as file:
    contents = file.read()

data = json.loads(contents)
print(data)

for question in data:
    print(question["question_text"])
    for alternatives in data:
        print(alternatives["Alternatives"])