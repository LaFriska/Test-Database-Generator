import json
import util

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

sqlFile.close()

