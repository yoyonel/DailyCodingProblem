# -*- encoding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

# https://docs.python.org/3/distutils/setupscript.html
setup(
    name='daily-coding-problem',
    version='0.1.0',
    license='None',
    description='',
    author='Lionel Atty',
    author_email='yoyonel@hotmail.com',
    url='',
    packages=['dailycodingproblem.{}'.format(x) for x in find_packages('src/dailycodingproblem')],
    package_dir={'': 'src'},
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Utilities',
    ],
    keywords=[

    ],
    install_requires=[
        "attrs==17.4.0",
        "binarytree",
        "matplotlib",
        "scipy",
    ],
    extras_require={},
    entry_points={
        'console_scripts': [
            'p11 = dailycodingproblem.11.app:main'
        ]
    },
    python_requires='>=3.6'
)
