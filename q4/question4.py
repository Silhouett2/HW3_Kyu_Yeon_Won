def factorial(n):
    if n == 1 or n == 0:     
        return 1    # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)    # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함
for i in range(8):
    print(factorial(2*(i)))



def main():

    print("")



if __name__ == '__main__':

 

    main()