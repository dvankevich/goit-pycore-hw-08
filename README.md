# goit-pycore-hw-08

## Приклад роботи

```
Welcome to the assistant bot!
Enter a command: all
No contacts
Enter a command: help

    	add [ім'я] [телефон]: Додати або новий контакт з іменем та телефонним номером,
    		або телефонний номер к контакту який вже існує.
    	change [ім'я] [старий телефон] [новий телефон]: Змінити телефонний номер для вказаного контакту.
    	phone [ім'я]: Показати телефонні номери для вказаного контакту.
    	all: Показати всі контакти в адресній книзі.
    	add-birthday [ім'я] [дата народження]: Додати дату народження для вказаного контакту.
    	show-birthday [ім'я]: Показати дату народження для вказаного контакту.
    	birthdays: Показати дні народження, які відбудуться протягом наступного тижня.
    	hello: Отримати вітання від бота.
    	help: Показати довідку.
    	close або exit: Закрити програму.

Enter a command: add Name01 1234567890
Contact added.
Enter a command: add Name02 0000000002
Contact added.
Enter a command: add Name03 0000000003
Contact added.
Enter a command: exit
Good bye!
```

```
Welcome to the assistant bot!
Enter a command: all
Contact name: Name01, birthday: None, phones: 1234567890
Contact name: Name02, birthday: None, phones: 0000000002
Contact name: Name03, birthday: None, phones: 0000000003
Enter a command: add-birthday Name01 23.08.1999
for Name01 birthday 23.08.1999 added
Enter a command: add-birthday Name02 06.09.2001
for Name02 birthday 06.09.2001 added
Enter a command: add-birthday 06.04.1995
Argument expected. Use help command for help.
Enter a command: add-birthday Name03 06.04.1995
for Name03 birthday 06.04.1995 added
Enter a command: add Name01 1000000001
Contact updated.
Enter a command: phone Name01
1234567890; 1000000001
Enter a command: birthdays
Name03 07.04.2025
Enter a command: exit
Good bye!
```

```
Welcome to the assistant bot!
Enter a command: all
Contact name: Name01, birthday: 23.08.1999, phones: 1234567890; 1000000001
Contact name: Name02, birthday: 06.09.2001, phones: 0000000002
Contact name: Name03, birthday: 06.04.1995, phones: 0000000003
Enter a command: exit
Good bye!
```
