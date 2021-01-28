import sqlite3
from random import randint

students = [(1001, 'Akash Nikam', 'akash@gmail.com', 'pass0000'), (1002, 'Sai Mahale', 'sai@gmail.com', 'pass0000'),
          (1003, 'Ganesh Patil', 'ganesh@gmail.com', 'pass0000'), (1004, 'Vishal Kumar', 'vishal@gmail.com', 'pass0000'),
          (1005, 'Satish Mane', 'satish@gmail.com', 'pass0000'), (1006, 'Kiran Kumar', 'kiran@gmail.com', 'pass0000'),
          (1007, 'Saurabh Thorat', 'saurabh@gmail.com', 'pass0000'), (1008, 'Akshay Ugale', 'akshay@gmail.com', 'pass0000'),
          (1009, 'Sagar Thore', 'sagar@gmail.com', 'pass0000'), (1010, 'Pradum Bawane', 'pradum@gmail.com', 'pass0000'),
          (1011, 'Mangesh Chavan', 'mangesh@gmail.com', 'pass0000'), (1012, 'Baban Kale', 'baban@gmail.com', 'pass0000'),
          (1013, 'Hari Dange', 'hari@gmail.com', 'pass0000'), (1014, 'Sunil Mahajan', 'sunil@gmail.com', 'pass0000'),
          (1015, 'Naresh Gore', 'naresh@gmail.com', 'pass0000')]

faculty = [(101, 'Akash Nikam', 'akash@gmail.com', 'pass0000'), (102, 'Parag Joshi', 'parag@gmail.com', 'pass0000'),
         (103, 'Vinayak Mali', 'vinayak@gmail.com', 'pass0000'), (104, 'Deepak Desale', 'deepak@gmail.com', 'pass0000'),
         (105, 'Vishnu Shastri', 'vishnu@gmail.com', 'pass0000'), (106, 'Sandip Dahatonde', 'sandip@gmail.com', 'pass0000')]


years = [2021]
months = [1]
days = [26, 27, 28]


conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()
insert = "INSERT INTO attendance(type,user_id,name,attendance,date,month,year) VALUES( 'faculty', ?, ?, ?, ?, ?, ? );"

for year in years:
    for month in months:

        for day in days:
            print(day)
            for student in faculty:
                x = randint(0, 1)
                cursor.execute(insert,(student[0], student[1], x, day, month, year))
                conn.commit()

conn.close()