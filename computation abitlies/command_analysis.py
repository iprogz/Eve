# command_analysis.py
def parse_command_line(command_line):
    components = command_line.split()
    command = components[0]
    parameters = components[1:]
    return command, parameters

def parse_log_file(file_path):
    commands = []
    with open(file_path, 'r') as file:
        for line in file:
            command, parameters = parse_command_line(line.strip())
            commands.append({'command': command, 'parameters': parameters})
    return commands

def analyze_commands(commands):
    command_frequency = {}
    for command_info in commands:
        command = command_info['command']
        command_frequency[command] = command_frequency.get(command, 0) + 1
    return command_frequency

