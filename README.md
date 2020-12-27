# TensorFlow Protobuf

Imagine you want to talk to your model deployed with TF-Serving using gPRC and protobuf.

To convert your NumPy array, you'd need to use `make_tensor_proto` function:

```python
import tensorflow as tf

def np_to_protobuf(data):
    return tf.make_tensor_proto(data, shape=data.shape)
```

Boom - you have a 2 GB dependency to deal with! 


This project takes only the part you actually need for that: the protobuf files (compiled). 

With it, your code will look like that:

```python

```

A bit more verbose, but without the 2GB baggage. 

Have fun!


# Process

To see how we extract and compile the protobuf files, check [tf-serving-proto.sh](tf-serving-proto.sh).

To use it:

```bash
TF_VERSION="2.3.0" ./tf-serving-proto.sh
```
