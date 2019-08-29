
# Define a Python class named Student. This class will have 5 properties.

# 1. First name (string)
# 2. Last name (string)
# 3. Age (integer)
# 4. Cohort number (integer)
# 5. Full name (read-only string)

# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.
# The full name property should return first name and last name separated by a space. It's value cannot be set.

class Student:
    # First Name
    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return ""

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Please provide a string value for the first name')
    #Last Name
    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('Please provide a string value for the last name')
    #Age
    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please provide an integer value for the age')
    #Cohort Number
    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return 0

    @cohort_number.setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError('Please provide an integer value for the cohort number')

    #Full name read only
    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return ""

    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_number}."

ron = Student()
ron.first_name = "Ron"
ron.last_name = "Gates"
ron.age = 72
ron.cohort_number = 43

print(ron.first_name)
print(ron.full_name)
print(ron)

# Use the __str__ and __repr__ magic methods on your class to specify what an object's string representation should be. It's just like the toString() method in JavaScript.

# If you print a Student object. The output would look something like below.

# mike = Student()
# mike.first_name = "Mike"
# mike.last_name = "Ellis"
# mike.age = 35
# mike.cohort_number = 39

# print(mike)
# <__main__.Student object at 0x107133f60>
# But if you specify exactly what string should be returned from __str__ or __repr__, that will print out instead. If you implement the following method on your class...

# class Student:

#     def __str__(self):
#         return f"{self.full_name}"
# then the output will change

# print(mike)
# Mike Ellis
# Change your class so that any objects created from it will be rerpesented as strings in the following format.

# Mike Ellis is 35 years old and is in cohort 39

