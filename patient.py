# Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization

# 1. Social security number
# 2. Date of birth
# 3. Health insurance account number
# 4. First name
# 5. Last name
# 6. Address

# The first three properties should be read-only. First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name. Address should have a
#getter and setter.

class Patient:
    def __init__(self, social, birthday, insurance_num, first_name, last_name, address):
        self.__social_security_number = social
        self.__date_of_birth = birthday
        self.__insurance_number = insurance_num
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address


    @property
    def social_security_number(self):
        try:
            return self.__social_security_number
        except AttributeError:
            return ""

    @property
    def date_of_birth(self):
        try:
            return self.__date_of_birth
        except AttributeError:
            return ""

    @property
    def insurance_number(self):
        try:
            return self.__insurance_number
        except AttributeError:
            return ""

    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return ""

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return ""

    @address.setter
    def address(self, new_address):
        if type(new_address) is str and int:
            self.__address = new_address
        else:
            raise TypeError('Please provide a house number and street name')

cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
# cashew.social_security_number = "838-31-2256"

# Neither should this
# cashew.date_of_birth = "01-30-90"

# But printing either of them should work
print(cashew.social_security_number)   # "097-23-1003"

# These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"
