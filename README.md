# dmp-common-client
This is a template repository that can be be used to generate new repositories with the same directory structure, branches, and files. For git, we recommend using [Github Flow](https://guides.github.com/introduction/flow/)

## Issue

Please report all features, bugs, and improvement to rdar://component/issues.


## Get Started
1. change version number in `VERSION` or add env params `BASE_VERSION`
2. append install_requires list in `setup.py` (if has)
3. `python setup.py sdist bdist_wheel`
4. `python3 -m twine upload --config-file ~/.pypirc --repository apple-pypi dist/* --verbose`