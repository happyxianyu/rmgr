rmdir dist -r
rmdir rmgr.egg-info -r
rmdir build -r
python setup.py sdist bdist_wheel
@REM python -m twine upload --repository testpypi dist/*
@REM twine upload dist/*

