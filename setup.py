import os
from setuptools import setup, find_packages


directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setup(
    name='mcnotify',
    version='0.1.0',
    description='A notification daemon for minecraft servers',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Tomasz "TFKls" Kulis',
    author_email='tfk@tfkls.dev',
    python_requires='>=3.6.0',
    url='https://github.com/TFKls/mcnotify',
    license='GPLv3',
    entry_points = {
	"console_scripts": [
	    "mcnotify = mcnotify:main"
	]
    },
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Microsoft :: Windows :: Windows 10',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
