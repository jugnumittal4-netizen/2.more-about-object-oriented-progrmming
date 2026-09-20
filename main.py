class employee():
    def __init__(self):
        print("Employee class initialized")
    def __del__(self):
        print("Employee class destroyed")
def create_object():
    print("Creating an employee...")
    ved = employee()
    print("destructor called.")
    return ved
print("Calling create_object() function...")
obj = create_object()
print("Program end...")