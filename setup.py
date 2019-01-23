
import os
import re
from setuptools import setup

def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')

VERSION = get_version('usm_registration_form', '__init__.py')

setup(
    name='usm_registration_form',
    version=VERSION,
    description='LMS - Registration Extension Form for USM',
    packages=['usm_registration_form'],
    install_requires=[
        'Django',
    ],
)
