#wap to generate fbonacci_generator


def fib_gen():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a + b


generator = fib_gen()
m = int(input("\nenter number to stop the series: "))
for i in range (m):
    print(next(generator))
    
