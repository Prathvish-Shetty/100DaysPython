"""
import smtplib

my_email = "psscode1@gmail.com"
password = "euaqsnnfjeugzwqs"


# # email provider smtp server
# connection = smtplib.SMTP("smtp.gmail.com")
# # make connection secure
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="prathvishshetty808@gmail.com",
#                     msg="Subject:Hello\n\nThis is the body of my email")
# connection.close()


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="prathvishshetty808@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email"
    )
"""

"""
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# print(day_of_week)
# print(now)
# print(year)
# print(type(year))
# print(type(now))

date_of_birth = dt.datetime(year=2000, month=1, day=1, hour=4)
print(date_of_birth)
"""
