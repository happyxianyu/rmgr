rmdir dist -r
python setup.py sdist bdist_wheel
@REM python -m twine upload --repository testpypi dist/*
@REM twine upload dist/*

