0.2.1 (2020-08-04)
==================

- Depend directly on ``pytest``.
  See https://github.com/mmerickel/pytest-venv/pull/2

- Add support for Python 3.6, 3.7, and 3.8.
  See https://github.com/mmerickel/pytest-venv/pull/2

0.2 (2016-11-27)
================

- Add ``VirtualEnvironment.get_version`` for querying versions from
  installed packages in the virtual environment.

- Support custom python interpreter paths via
  ``VirtualEnvironment.create(python=...)``.

0.1.1 (2016-11-27)
==================

- Ensure the virtual environment is started with the same Python executable
  as the current process.

0.1 (2016-11-27)
================

- Initial release.
