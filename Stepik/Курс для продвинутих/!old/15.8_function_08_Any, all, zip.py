


def ignore_command(command):
    ignore = ['alias', 'configuration', 'ip', 'sql', 'select', 'update', 'exec', 'del', 'truncate']
    return any(map(lambda x: x in command, ignore))


print(ignore_command('get ip'))  # True
print(ignore_command('select all'))  # True
print(ignore_command('delete'))  # True
print(ignore_command('trancate'))  # False
