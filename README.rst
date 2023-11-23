===========
pytest-venv
===========

.. image:: https://img.shields.io/pypi/v/pytest-venv.svg
    :target: https://pypi.python.org/pypi/pytest-venv

.. image:: https://github.com/mmerickel/pytest-venv/actions/workflows/ci-tests.yml/badge.svg?branch=main
    :target: https://github.com/mmerickel/pytest-venv/actions/workflows/ci-tests.yml?query=branch%3Amain

``pytest-venv`` is a simple pytest plugin that exposes a ``venv`` fixture.
The fixture is used to create a new virtual environment which can be used
to install packages and run commands inside tests.

Usage
=====

.. code-block:: python

    import os

    def test_it(venv):
        venv.install('pyramid', upgrade=True)
        subprocess.check_call(
            [os.path.join(venv.bin, 'pserve'), 'development.ini'],
        )

API
===

The ``venv`` fixture is an instance of
``pytest_venv.VirtualEnvironment(path)`` which exposes the following API:

``path``

  The path to the virtualenv directory.

``bin``

  The path to the bin / Scripts directory.

``python``

  The path to the python executable in the virtualenv.

``create(system_site_packages=False, python=None, *, extra_args=None)``

  Create a virtualenv. This is called automatically by the ``venv`` fixture.
  If ``python`` is ``None`` then the virtual environment will be created
  using the same executable as the active runtime.

``install(pkg_name, editable=False, upgrade=False, *, extra_args=None)``

  Use pip to install a package into the virtualenv. ``pkg_name`` may be a
  path to a package on disk.

``get_version(pkg_name, *, raises=True)``

  Returns a ``packaging.version.Version`` object which is sortable and
  convertable to a string.
