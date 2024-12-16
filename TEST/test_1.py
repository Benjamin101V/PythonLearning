start=1900;end=2021
sum=0
for year in range(1900,2021):
    if year%4 == 0 and year%100 != 0:
        print(year,end=' ')
        sum+=1
    elif year%400 ==0:
        print(year,end=' ')
        sum+=1
print(f'\nSum of leap years from {start} to {end} is {sum}')