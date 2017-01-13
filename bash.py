# -*- coding: utf-8 -*-

def bash(bashCommand, display=True, returnString=False):
    """Runs bash commands from the Python interpreter.
    args:
    bashCommand -- the bash command to execute
    display -- displays the ouptput of the command
    returnString -- returns the output of the command as a string
    """
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = str(process.communicate()[0])
    if display:
        print(output)
    if returnString:
        return output