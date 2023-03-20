# Grass salary program
emp = input('Enter EMP Name: ')
basic_salary = int( input('Enter Your Basic Salary: '))
p_days = int( input('Enter Pressent Days: '))

oneday_amount = basic_salary/30
absent_days = 30 - p_days
absent_amount =oneday_amount * absent_days

medical = basic_salary * 20 /100
conveyance = basic_salary * 40 /100
uniform_allowance = basic_salary * 10 /100

print('Employee name is ' , emp)
print(f'Medical Allowance is = {medical}')
print(f'Conveyance Allowance is = {conveyance}')
print(f'Uniform Allowance is = {uniform_allowance}')
gross = basic_salary+medical+conveyance+uniform_allowance-absent_amount
income_tax= gross * 0.02
net_salary = (gross - income_tax)
if(p_days == 30):
    print(f'Net Salary is =  {net_salary}')
    bonous = basic_salary * 0.1
    print(f'Bonous amount = {bonous}')
    print(f'congratulation you are present 30 days and you are received 10 % bonous: Net Salary = {net_salary + bonous}')
else:
    print('Sorry your Attendance did not complete and You did not receive Bonous ')
    print(f'Net Salary is =  {net_salary}')