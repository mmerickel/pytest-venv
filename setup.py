from setuptools import setup, find_packages

def readfile(name):
    with open(name) as f:
        return f.read()

readme = readfile('README.rst')
changes = readfile('CHANGES.rst')

requires = [
    'pytest',
    'setuptools',
    'virtualenv',
]

tests_require = [
    'coverage',
]

setup(
    name='pytest-venv',
    version='0.2.1',
    description='py.test fixture for creating a virtual environment',
    long_description=readme + '\n\n' + changes,
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
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
