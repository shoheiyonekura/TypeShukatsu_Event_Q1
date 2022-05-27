for num in range(1, 101):
    string = ''

    # ここから記述
    if num % 3 == 0 and num % 15 != 0: #3の倍数かつ15の倍数ではない
        string = 'Fizz'
    elif num % 5 == 0 and num % 15 != 0: #5の倍数かつ15の倍数ではない
        string = 'Buzz'
    elif num % 15 == 0: #15の倍数
        string = 'FizzBuzz'
    else:
        print(num, end = "")
    # ここまで記述

    print(string)