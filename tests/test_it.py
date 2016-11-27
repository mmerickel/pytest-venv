import sys
import subprocess

def test_it(venv):
    result = subprocess.check_output(
        [venv.python, '-c', 'print("hello world")'],
    )
    assert b'hello world' in result

def test_it_installs_dep(venv):
    venv.install('pyramid')
    subprocess.check_call([venv.python, '-c', 'import pyramid'])

def test_it_uses_correct_python(venv):
    result = subprocess.check_output(
        [venv.python, '-c', 'import sys; print(sys.version)'],
    )
    assert result.decode('utf8').strip() == str(sys.version)
