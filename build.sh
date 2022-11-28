export TF_VERSION=2.11.0

echo "__version__ = '${TF_VERSION}'" > version.py

python -m venv env
source env/bin/activate

./tf-serving-proto.sh

pip install wheel twine

python setup.py sdist bdist_wheel

twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*

twine upload dist/*

rm -rf tensorflow/ tensorflow_serving/
rm -rf tensorflow_protobuf.egg-info/ build/ dist/ __pycache__/
rm version.py LICENSE