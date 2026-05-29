# Python Adventures
hello_world, name = ('Hello world', 'Daniel')
print('<----Strings---->')
print('')

print(hello_world[0])
print(hello_world[1])
print(hello_world[2])
print(hello_world[3])
print('')
print('<----for loop---->')
print('')

count = 0
for i in hello_world:
    count += 1
    print(i) # + f' {count}'

print('')

print('<----Maths---->')
print('')
    
def adding(num_1, num_2):
    """
    simple function, 
    which adds two numbers together
    and prints out the result as a string value
    """
    answer = num_1 + num_2

    print(f"{num_1} + {num_2} = {answer}")

adding(5,2)
print('what does the function mathmatics do?: ', adding.__doc__)

print('')
print(f"Name: {name}")
