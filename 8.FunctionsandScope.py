# Functions and Scope

def greet(name):
    greeting = f"Hello, {name}!"
    return greeting

# Scope Example
def outer_function():
    outer_var = "I'm outside!"
    
    def inner_function():
        inner_var = "I'm inside!"
        print(inner_var)
        print(outer_var)
    
    inner_function()

print(greet("Alice"))
outer_function()
