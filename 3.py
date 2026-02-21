employee_name=input("enter your name: ")
salary_expectation=int(input("enter your salary expectation: "))
employee_name2=input("enter your name: ")
salary_expectation2=int(input("enter your salary expectation: "))
#abs is used to give absolute value
salary_expectation_difference= abs(salary_expectation2 - salary_expectation)



print(f'{employee_name} needs {salary_expectation} and {employee_name2} needs {salary_expectation2} final difference is{salary_expectation_difference}')