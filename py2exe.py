from cx_Freeze import setup, Executable

setup(name = 'ats',
    version = '0.1',
    description = 'executatable file',
    executables = [Executable('keyStroke.py')]
    )