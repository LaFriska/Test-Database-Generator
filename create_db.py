import json
import util
import random

courses = json.load(open("courses.json"))

initial = """
--WARNING!
--DO NOT EXECUTE THIS FILE ON A DATABASE SERVER IF
--TABLES WITH THE NAME "course", "staff" and "teach"
--ARE KEPT, UNLESS THESE TABLES ARE FOR THE SOLE PURPOSE
--OF COMP2400 EXAM REVISION. RUNNING THIS FILE DROPS ALL
--THREE TABLES.

DROP TABLE course CASCADE;
DROP TABLE staff CASCADE;
DROP TABLE teach CASCADE;

create table staff (
  uid char(8) primary key,
  name text not null
);
create table course (
  ccode char(8) primary key,
  name text not null,
  level integer
);
create table teach (
  uid char(8) not null references staff(uid),
  ccode char(8) not null references course(ccode),
  sem char(2) check (sem = 'S1' or sem = 'S2'), -- sem can only take values 'S1' or 'S2'
  year integer,
  role text not null,
  primary key (uid, ccode, sem, year)
);
"""

sqlFile = open('testdb.sql', 'w')

#Writes initial statements.
sqlFile.write(initial)

for course in courses:
    if len(course["CourseCode"]) == 8:
        ccode = course["CourseCode"]
        name  = course["Name"]
        level = util.getCourseLevel(ccode)
        sqlFile.write(f"INSERT INTO course (ccode, name, level) VALUES ('{ccode}', '{util.sanitize(name)}', {level});" + "\n")


conv = json.load(open("randomConveners.json", 'r')) #There are 1724 conveners. Conveners have uid starting with 9254
tutors = json.load(open("randomTutors.json", 'r')) #There are 1024 tutors. Tutors have uid starting with 2368

CHeader = 92540000
THeader = 23680000

comment = """

--Insertions for conveners. 

"""
sqlFile.write(comment)

for i in range(len(conv)):
    sqlFile.write(f"INSERT INTO staff (uid, name) VALUES ('{CHeader + i}', '{util.sanitize(conv[i])}');" + "\n")

comment = """

--Insertions for tutors. 

"""
sqlFile.write(comment)

for i in range(len(tutors)):
    sqlFile.write(f"INSERT INTO staff (uid, name) VALUES ('{THeader + i}', '{util.sanitize(tutors[i])}');" + "\n")

#def addRandomisedTeach(year, sem):
#    idArray = []
#    for course in courses:


sqlFile.close()

