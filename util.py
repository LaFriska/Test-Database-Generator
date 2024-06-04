def getCourseLevel(ccode):
    return int(ccode[4]) * 1000

def sanitize(input_string):
    sanitized_string = input_string.replace("'", "")
    return sanitized_string