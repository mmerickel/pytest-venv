import os
import packaging.version as pv
import pytest
import subprocess
import sys
import textwrap

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

    def create(self, system_packages=False, python=None, *, extra_args=None):
        cmd = [sys.executable, '-m', 'virtualenv']
        cmd += ['-p', python or sys.executable]
        if system_packages:
            cmd += ['--system-site-packages']
        if extra_args:
            cmd += extra_args
        cmd += [self.path]
        subprocess.check_call(cmd)

    def install(
        self, pkg_name, editable=False, upgrade=False, *, extra_args=None
    ):
        cmd = [self.python, '-m', 'pip', 'install']
        if upgrade:
            cmd += ['-U']
        if extra_args:
            cmd += extra_args
        if editable:
            cmd += ['-e']
        cmd += [pkg_name]
        subprocess.check_call(cmd)

    def get_version(self, pkg_name, *, raises=True):
        script = textwrap.dedent(
            f'''
            try:
                from importlib.metadata import version
            except ImportError:
                import pkg_resources
                version = lambda x: pkg_resources.get_distribution(x).version

            try:
                print(version("{pkg_name}"))
            except Exception:
                print('')
            '''
        )
        version = subprocess.check_output([self.python, '-c', script]).strip()
        if not version:
            if raises:
                raise Exception('package is not installed')
            return None
        return pv.Version(version.decode('utf8'))
