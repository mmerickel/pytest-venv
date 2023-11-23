import os
import pytest
import subprocess
import sys

here = os.path.abspath(os.path.dirname(__file__))


def test_it(venv):
    result = subprocess.check_output(
        [venv.python, '-c', 'print("hello world")'],
    )
    assert result.strip() == b'hello world'


def test_it_installs_dep(venv):
    venv.install('webob')
    subprocess.check_call([venv.python, '-c', 'import webob'])


def test_it_installs_dep_with_extra_args(venv):
    venv.install('webob', extra_args=['--prefer-binary'])
    subprocess.check_call([venv.python, '-c', 'import webob'])


@pytest.mark.skipif(
    sys.version_info < (3, 12), reason="Make sense only for Python 3.12"
)
def test_it_installs_dep_without_setuptools(venv):
    # micropipenv does not depend on setuptools
    # so this test verifies that `get_version` works
    # fine even when setuptools/pkg_resources are
    # not available in the virtual environment.
    venv.install('micropipenv')
    subprocess.check_call([venv.python, '-c', 'import micropipenv'])
    venv.get_version('micropipenv')


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


def test_get_version_returns_none(venv):
    version = venv.get_version('pyramid', raises=False)
    assert version is None


def test_get_version_raises(venv):
    with pytest.raises(Exception, match='package is not installed'):
        venv.get_version('pyramid')


def test_it_creates_with_system_packages(tmpdir):
    from pytest_venv import VirtualEnvironment

    venv = VirtualEnvironment(tmpdir.strpath)
    venv.create(system_packages=True, extra_args=['--no-setuptools'])

    result = subprocess.check_output(
        [venv.python, '-c', 'print("hello world")'],
    )
    assert b'hello world' in result
