

https://pypi.python.org/pypi/sherlok/

## shorter: http://stackoverflow.com/a/4157080/125617

    change (increase) version id in `setup.py`

    python setup.py sdist register upload

## longer:


https://packaging.python.org/en/latest/distributing.html


Working in “Development Mode”

    python setup.py develop


Register project in Pip

    python setup.py register


Packaging your Project

    python setup.py sdist

Pure Python Wheels

    python setup.py bdist_wheel

Upload

    twine upload dist/*

