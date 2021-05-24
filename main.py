import json


def judge(problem_list, requested_desc: str):
    for i in problem_list:
        for j in problem_list[i]:
            if j['topic'].find(requested_desc) != -1:
                for k in j['options']:
                    if k[:1] == j['answer']:
                        print(k)
                return
    print("Not Found.")


def review_problem(problem):
    print(problem['topic'])
    for i in problem['options']:
        print(i)
    answer = input("Please fill in your answer: ")
    if answer == problem['answer']:
        print("Correct!")
    else:
        print("Not correct. Correct answer: " + problem['answer'])
    print('')


with open('problem_list.json') as f:
    problem_list = json.load(f)
    command = input("Welcome to this project. Please choose [R]eview, [C]heck_problem: ")
    if command == 'R' or command == 'r':
        chapter = input("Please choose the chapter: ")
        for i in problem_list[chapter]:
            review_problem(i)
    elif command == 'C' or command == 'c':
        requested_desc = input("Paste your problem description here: ")
        while True:
            judge(problem_list, requested_desc)
