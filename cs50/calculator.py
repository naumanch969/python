def main():
    x = int(input("what's x? "))
    print(f'square of {x} is',square(x))
 
def square(n):
    return n + n

if __name__ == '__main__':
    main()