# Một đoạn code sử dụng hàm def 
# Kiểm tra đầu ra các số chia hết cho 3 , 5
# 3 - Fizz 5 - Buzz all - FizzBuzz
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 ==0):
        return 'FizzBuzz'
    if input % 3 == 0:
        return 'Fizz'
    if input % 5 == 0:
        return 'Buzz'
    return input
print(fizz_buzz(15))