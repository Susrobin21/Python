#Fizzbuzz game

for num in range(0,100):
    if num%3 == 0 and num%5 ==0:
        print('Fizzbuzz')
    elif num%3 ==0:
        print('Fizz')
    elif num%5 == 0:
        print('Buzz')
    else :
        print(num)
print(num)