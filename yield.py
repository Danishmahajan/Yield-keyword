def table_print(n):
    for i in range(1,10):
        yield i*n
        print( end="   ") 
        yield i*n*2

for item in table_print(int(input("Enter a value: "))):
    print(item)