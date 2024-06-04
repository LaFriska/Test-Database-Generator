# Test DB Generator for COMP2400 Sample Exam

I used Python, a JSON file of each ANU course, and a randomly generated list (by generative AI)
of plausible human names to create a set of insert statements that act as a sample database for the example
exam questions. This project aims to support fellow COMP2400 students.

To load the sample database, simply execute the (18,000 lines of) queries in 
`testdb.sql`. **DO NOT** run this file unless you are sure the database server you are 
running this on will not get impacted by the first 3 statements, which immediately deletes
any tables named `staff`, `teach` and `course`. 

Note that the course codes are actual ANU courses, while the conveners and tutors are completely
made up. This database is **NOT** a source of accurate information for ANU courses. 