# def create_user_request(name, password):
#     new_user = User(name, password)
#     request = consrtuct_request(new_user)
#     add_to_log(request)
#     response = execute_request(request)
#     add_to_log(response)
#
# @llog_api_calls
# def create_user_request(namme, password):
#     new_user = User(name, password)
#     request = construct_request(request)
#     response = execute_request(request)
# @log_execution_time


def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello))
print(greet_bob(be_awesome))



#как вызвать из консоли?
# greet_bob(say_hello)
# 'Hello Bob'
# >>> greet_bob(be_awesome)
# 'Yo Bob, together we are the awesomest!'
