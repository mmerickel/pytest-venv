from setuptools import find_packages, setup


def readfile(name):
    with open(name) as f:
        return f.read()


readme = readfile('README.rst')
changes = readfile('CHANGES.rst')

requires = [
    'packaging',
    'pytest',
    'virtualenv',
]

tests_require = [
    'coverage',
]

setup(
    name='pytest-venv',
    version='0.3',
    description='py.test fixture for creating a virtual environment',
    long_description=readme + '\n\n' + changes,
    long_description_content_type='text/x-rst',
    author='Michael Merickel',
    author_email='michael@merickel.org',
    url='https://github.com/mmerickel/pytest-venv',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requires,
    extras_require={
        'testing': tests_require,
    },
    zip_safe=False,
    keywords='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Testing',
    ],
    entry_points={
        'pytest11': [
            'venv = pytest_venv',
        ],
    },
)
