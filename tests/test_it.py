import os
import sys
import subprocess

here = os.path.abspath(os.path.dirname(__file__))


def test_it(venv):
    result = subprocess.check_output(
        [venv.python, '-c', 'print("hello world")'],
    )
    assert result.strip() == b'hello world'


def test_it_installs_dep(venv):
    venv.install('pyramid')
    subprocess.check_call([venv.python, '-c', 'import pyramid'])


def test_it_installs_editable_dep(venv):
    venv.install(os.path.join(here, 'myapp'), editable=True)
    result = subprocess.check_output([venv.python, '-c', 'import myapp'])
    assert result.strip() == b'hello world'


def test_it_upgrades_dep(venv):
    venv.install('pyramid==1.6')
    version1 = venv.get_version('pyramid')
    assert str(version1) == '1.6'
    venv.install('pyramid', upgrade=True)
    version2 = venv.get_version('pyramid')
    assert version2 > version1


def test_it_uses_correct_python(venv):
    result = subprocess.check_output(
        [venv.python, '-c', 'import sys; print(sys.version)'],
    )
    assert result.decode('utf8').strip() == str(sys.version)


def test_it_creates_with_system_packages(tmpdir):
    from pytest_venv import VirtualEnvironment

    venv = VirtualEnvironment(tmpdir.strpath)
    venv.create(system_packages=True)

    result = subprocess.check_output(
        [venv.python, '-c', 'print("hello world")'],
    )
    assert b'hello world' in result
