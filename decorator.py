# a decorator is a callable that returns a callable
# Basically, a decorator takes in a function, adds
# some functionality and returns it


def change(f):
    def wrapper():
        print("This goes first")
        f()
        print("This goes last")

    return wrapper


@change
def message():
    print("You know what happened")


message()

