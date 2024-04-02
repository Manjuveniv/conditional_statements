#if condition
age=int(input('enter number:'))
if age>18:
    print('eligible for the vote')
    
# finding leap year-using if-else
year=int(input('enter year:'))
if (year%100==0 and year%400==0) or (year%100!=0 and year%4==0):
    print('leap year')
else:
    print('not a leap year')
    
# find max num among 4 numbers - using if elif
n1=int(input('enter number:'))
n2=int(input('enter number:'))
n3=int(input('enter number:'))
n4=int(input('enter number:'))
if n1==n2==n3==n4:
    print('all are same')
elif n1>n2 and n1>n3 and n1>n4:
    print('n1 is max number')
elif n2>n3 and n2>n4:
    print('n2 is max number')
elif n3>n4:
    print('n3 is max number')
else:
    print('n4 is max number')

# output

#enter number:6
#enter number:9
#enter number:8
#enter number:10
#n4 is max number



