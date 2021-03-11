# function return another function


def is_called():
    def is_returned():
        print("This is return function")

    return is_returned


returned = is_called()

returned()
