# Quiz 1
# For each .csv file, find the total number of rows
# and the number of unique students

import unicodecsv

def read_csv(filename):
    '''
    create a function to read csv file
    input : .csv tables
    output : return list of table data
    '''
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

# Here I'm printing out number of rows in each table
    # number of rows
print len(enrollments)
print len(daily_engagement)
print len(project_submissions)

print           # extra line spacing

# finding number of unique students in each table
    # enrollment table
unique_enrolled_students = set()
for enrollment in enrollments:
    unique_enrolled_students.add(enrollment["account_key"])
print len(unique_enrolled_students)

    # daily_engagement table
unique_engagement_students = set()
for engagement in daily_engagement:
    unique_engagement_students.add(engagement["acct"])
print len(unique_engagement_students)

    # project_submissions table
unique_submissions_students = set()
for submission in project_submissions:
    unique_submissions_students.add(submission["account_key"])
print len(unique_submissions_students)

print
'''
Notice I'm doing a lot of repetition work above for the three tables
The reason is because two tables had 'account_key' while the other had 'acct'
However, this problem can be easily solved by creating a new 'account_key'
column in the daily_engagement table, copy all data from the 'acct' column into
it and then delete the 'acct' column.
'''
for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]

print daily_engagement[0]['account_key']
