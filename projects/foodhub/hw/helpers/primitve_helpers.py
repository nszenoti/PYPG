def snake_to_pascal(snake_str, join_with=' '):
    ''' Convert snake_case to PascalCase (eg my_name -> MyName)
    Args:
        snake_str (str): string to convert
        join_with (str): character to join the components, default is space
    '''
    components = snake_str.split('_')
    return join_with.join(x.title() for x in components)