def snake_to_camel(n):

    comp = n.split('_')
    return comp[0] + ''.join(x.title() for x in comp[1:])

# example 
snake = "my_super_var"

x = snake_to_camel(snake)

print(x)