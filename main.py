import pandas
import datetime as dt
import random
import smtplib
from cryptography.fernet import Fernet
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

key = Fernet.generate_key()
print(key)


name_string = None
email_string = None

def check_csv():
    global name_string
    global email_string

    convert_l_dict = df.to_dict(orient="records")
    #print(convert_l_dict)
    for index in range(len(convert_l_dict)):
        #print(convert_l_dict[index])
        #print(convert_l_dict[index]["day"])
        if convert_l_dict[index]["month"] == month_now and convert_l_dict[index]["day"] == day_now:
            name_string = convert_l_dict[index]["name"]
            email_string = convert_l_dict[index]["email"]
            return True



def send_email():
    my_email = "956@gmail.com"
    password = "app password --- search google and find  "

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_string,msg=f"Subject:Happy Birthday to You \n\n {update_letter}")






list_letters =["letter_1.txt","letter_2.txt","letter_3.txt"]
df = pandas.read_csv("birthdays.csv")
now = dt.datetime.now()
month_now = now.month
day_now = now.day
if check_csv():
    random_letter = random.choice(list_letters)

    with open(f"letter_templates/{random_letter}") as f:
        letter = f.read()
        update_letter = letter.replace("[NAME]",name_string)
        send_email()

#


