from datetime import datetime, timedelta
def is_date_passed(date, today):
    if (today.month > date.month) or (today.month == date.month and today.day > date.day):
        return True # The date has already been
    return False # The date is today or will be in the future.

def get_upcoming_birthdays(users):
    '''
        returns a list of everyone whose birthday is 7 days in the future, including 
        the current day. if the birthday falls on a weekend, the date of the congratulation
        is postponed to the next working day.
        Args:
            users (list of dict): A list of dictionaries, where each dictionary represents a user.
                Each dictionary should contain the following keys:
                - 'name' (str): user name
                - 'birthday' (str): YYYY.MM.DD 
                example: 
                    [
                        {"name": "John Doe", "birthday": "1985.01.23"},
                        {"name": "Jane Smith", "birthday": "1990.01.27"}
                    ]
        Returns:
            (list of dict): A list of dictionaries, where each dictionary represents a user info
                Each dictionary should contain the following keys:
                - 'name' (str): user name
                - 'congratulation_date' (str): YYYY.MM.DD
                example:
                    If today is 2024.01.22 the result could be:
                    [
                        {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
                        {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
                    ]
                    This list contains information about who and when to wish a happy birthday.
    '''
    congratulation_list = list()
    today = datetime.today().date()
    seven_days = timedelta(days=7)
    

    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        if not is_date_passed(user_birthday, today):
            if (is_date_passed(user_birthday, today + seven_days)):
                user_birthday_weekday = datetime(month=user_birthday.month, day=user_birthday.day, year=today.year).weekday()
                if user_birthday_weekday > 5:
                    days_to_monday = timedelta(days=7 - user_birthday_weekday)
                    user_congratulation_date = datetime(month=user_birthday.month, day=user_birthday.day, year=today.year) + days_to_monday
                else:
                    user_congratulation_date = datetime(month=user_birthday.month, day=user_birthday.day, year=today.year)

                if (is_date_passed(user_congratulation_date, today + seven_days)):
                    congratulation_list.append(dict({'name': user["name"], 'congratulation_date': user_congratulation_date.date().strftime("%Y.%m.%d")}))

    return congratulation_list


  

if __name__ == "__main__":
    #print(get_upcoming_birthdays.__doc__)
    users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.02.27"},
    {"name": "Jonh Connor", "birthday": "1990.03.02"},
    {"name": "Sarah Connor", "birthday": "1970.05.18"}
    ]
    print(get_upcoming_birthdays(users))
    today = datetime.today().date()

    assert is_date_passed(datetime(year=2019, month=1, day=7).date(), today) == True
    assert is_date_passed(datetime(year=2029, month=12, day=31).date(), today) == False


