import random

def getCourseLevel(ccode):
    return int(ccode[4]) * 1000

def sanitize(input_string):
    sanitized_string = input_string.replace("'", "")
    return sanitized_string

def getRandomConvenerNum():
    r = random.randint(1, 10)
    if r <= 50:
        return 1
    elif r <= 75:
        return 2
    elif r <= 92:
        return 3
    else:
        return 4