for num in range(1, 101):
    string = ''

    # ここから記述

    if num % 15 == 0:  # 15の倍数
        string = "FizzBuzz"

    elif num % 3 == 0:  # 3の倍数
        string = "Fizz"

    elif num % 5 == 0:  # 5の倍数
        string = "Buzz"

    else:  # それ以外
        string = num

    # ここまで記述

    print(string)
