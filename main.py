import pandas
import datetime as dt
import random
import smtplib
import os

print("RULEAZA ACEST MAIN.PY")
print("fisier:", __file__)
print("folder curent:", os.getcwd())

now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for index, data_row in data.iterrows()
}

print("today:", today)
print("keys:", birthdays_dict.keys())
print("match:", today in birthdays_dict)


if today in birthdays_dict:
    birthday_person = birthdays_dict[today]

    random_letter_number = random.randint(1, 3)

    with open(f"letter_templates/letter_{random_letter_number}.txt") as letter_file:
        letter_contents = letter_file.read()

    personalized_letter = letter_contents.replace("[NAME]", birthday_person["name"])

    my_email = os.environ.get("MY_EMAIL")
    password = os.environ.get("MY_PASSWORD")


    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
        )