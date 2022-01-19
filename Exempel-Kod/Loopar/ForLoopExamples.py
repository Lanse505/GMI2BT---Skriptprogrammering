import random

values = [{}]
languages = [{"Python", "Java", "JavaScript", "Ruby", "C#", "C++"}]

if __name__ == '__main__':
    for i in range(0, 25, 1):
      values.append(random.randint(0, 25))
    print(values)
    for language in languages:
      print(language)

    input()