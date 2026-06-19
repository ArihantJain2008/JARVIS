import subprocess


def open_notepad():

    subprocess.Popen(
        ["notepad.exe"]
    )

    return "Notepad opened."


def open_calculator():

    subprocess.Popen(
        ["calc.exe"]
    )

    return "Calculator opened."