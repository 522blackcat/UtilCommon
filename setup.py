import os
from codecs import open

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


def read_version():
    version = os.environ.get('BASE_VERSION')
    if version is not None:
        return version
    version_py = os.path.join(here, 'VERSION')
    with open(version_py, encoding='utf-8') as f:
        first_line = f.readline()
        return first_line.strip()


github_url = 'https://github.com/522blackcat/UtilCommon'


setup(
    name='UtilCommon',
    version=read_version(),

    description='person unit client ',

    url=github_url,
    packages=find_packages('../..', exclude=['tests*']),
    python_requires='>=3.7, <4',
    install_requires=[
        'requests',
        'retry>=0.9.2',
    ],

    author='Xiangdong Liang',
    author_email='xiangdong_liang@apple.com',

    keywords='until security',
    test_suite='pytest'
)