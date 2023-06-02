# Define a function that has two parameters, year_of_birth and current_year .
# The current_year parameter should be a default parameter with the current year as a default value.
# The function should calculate and return the age of the user given the year of birth and the current year.

year_of_birth=int(input("Enter the birth year: "))
def yr(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    return  age



age=yr(year_of_birth)
print(age)

