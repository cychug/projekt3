# najprostrzy przykład

def function_performace(func):
    func()


def show_message():
    print("wiadmość")


function_performace(show_message)


# wywołanie funkcji z funkcjii z argumente3m

def function_performace(func, argument):
    func(argument)


def show_message(message):
    print(message)


function_performace(show_message, "This is message")
