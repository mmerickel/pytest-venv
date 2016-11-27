import os
import pkg_resources
import pytest
import sys
import subprocess

WIN = sys.platform == 'win32'


@pytest.fixture
def venv(tmpdir):
    venv = VirtualEnvironment(tmpdir.strpath)
    venv.create()
    yield venv


class VirtualEnvironment(object):
    def __init__(self, path):
        self.path = path
        self.bin = os.path.join(
            self.path,
            'bin' if sys.platform != 'win32' else 'Scripts',
        )
        self.python = os.path.join(self.bin, 'python')

    def create(self, system_packages=False, python=None):
        cmd = [sys.executable, '-m', 'virtualenv']
        cmd += ['-p', python or sys.executable]
        if system_packages:
            cmd += ['--system-site-packages']
        cmd += [self.path]
        subprocess.check_call(cmd)

    def install(self, pkg_name, editable=False, upgrade=False):
        cmd = [self.python, '-m', 'pip', 'install']
        if upgrade:
            cmd += ['-U']
        if editable:
            cmd += ['-e']
        cmd += [pkg_name]
        subprocess.check_call(cmd)

    def get_version(self, pkg_name):
        script = (
            'import pkg_resources; '
            'print(pkg_resources.get_distribution("%(pkg_name)s").version)'
        ) % dict(pkg_name=pkg_name)
        version = subprocess.check_output([self.python, '-c', script]).strip()
        return pkg_resources.parse_version(version.decode('utf8'))
