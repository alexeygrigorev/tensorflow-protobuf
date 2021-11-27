## TensorFlow Protobuf

Imagine you want to talk to your model deployed with TF-Serving using gPRC and protobuf.

To convert your NumPy array, you'd need to use `make_tensor_proto` function:

```python
import tensorflow as tf

def np_to_protobuf(data):
    return tf.make_tensor_proto(data, shape=data.shape)
```

Boom - you have a 2 GB dependency to deal with! 


## TensorFlow Protobuf

This project takes only the part you actually need for that: the protobuf files (compiled). 

### Installing it

```bash
pip install tensorflow-protobuf==2.3.0
```

Other available versions: 2.7.0

### Using it

With it, your code will look like that:


```python
from tensorflow.core.framework import tensor_pb2, tensor_shape_pb2, types_pb2


def dtypes_as_dtype(dtype):
    if dtype == "float32":
        return types_pb2.DT_FLOAT
    raise Exception("dtype %s is not supported" % dtype)


def make_tensor_proto(data):
    shape = data.shape
    dims = [tensor_shape_pb2.TensorShapeProto.Dim(size=i) for i in shape]
    proto_shape = tensor_shape_pb2.TensorShapeProto(dim=dims)

    proto_dtype = dtypes_as_dtype(data.dtype)

    tensor_proto = tensor_pb2.TensorProto(dtype=proto_dtype, tensor_shape=proto_shape)
    tensor_proto.tensor_content = data.tostring()

    return tensor_proto


def np_to_protobuf(data):
    if data.dtype != "float32":
        data = data.astype("float32")
    return make_tensor_proto(data)
```

A bit more verbose, but without the 2GB baggage. 

See a full example here: [example.py](example.py)

Have fun!


## Building and compiling it

To see how we extract and compile the protobuf files, check [tf-serving-proto.sh](tf-serving-proto.sh).

To use it:

```bash
TF_VERSION="2.3.0" ./tf-serving-proto.sh
```


## Publishing on PyPI

If you want to build it for other versions and publish it,
do this:

```bash
export TF_VERSION=2.3.0
echo ${TF_VERSION} > .version

python -m venv env
source env/bin/activate

./tf-serving-proto.sh

pip install wheel twine

python setup.py sdist bdist_wheel

twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*


rm -rf tensorflow/ tensorflow_serving/
rm -rf tensorflow_protobuf.egg-info/ build/ dist/ __pycache__/

```