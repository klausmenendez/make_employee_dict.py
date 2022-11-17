# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Employee:

    def __init__(self, name, id_number, salary, email_address):
        '''
        Creates employee object with name, id number, salary and email address

        '''
        self._name = name
        self._id_number = id_number
        self._salary = salary
        self._email_address = email_address

    def _name(self):  # return employee name
        return self._name

    def _id_number(self):  # return id
        return self._id_number

    def _salary(self):    # return employees salary
        return self._salary

    def _email_address(self):  # returns email address
        return self._email_address


id_database = {}


def make_employee_dict(names, id_numbers, salaries, email_addresses):
    for i in range(0, len(names)):
        id_database[id_numbers[i]] = Employee(names[i], id_numbers[i], salaries[i], email_addresses[i])
    return id_database


# result = make_employee_dict(["klaus", "sarah", "riley"], ["101", "102", "103"], [13.75, 15, 13.75], ["klaus@gmail.com", "sarah@gmail.com", "Riley@gmail.com"])
# print(result["103"].get_salary())
