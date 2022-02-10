# updat emy furure branch
def my_decorator(func):
    def wrapper():
        print(f'This is a decorator')
        func()
    return wrapper

@my_decorator
def func_test():
    print('Hello World')
