
set -e

TF_VERSION=${TF_VERSION:-2.3.0}
TFS_VERSION=${TFS_VERSION:-${TF_VERSION}}

echo "running tf-serving-proto.sh with TF_VERSION=${TF_VERSION} and TFS_VERSION=${TFS_VERSION}"

pip install grpcio-tools

wget https://github.com/tensorflow/tensorflow/archive/v${TF_VERSION}.zip -O tf.zip
unzip tf.zip && rm tf.zip

wget https://github.com/tensorflow/serving/archive/${TFS_VERSION}.zip -O tf-serving.zip
unzip tf-serving.zip && rm tf-serving.zip

mv serving-${TFS_VERSION}/tensorflow_serving tensorflow-${TF_VERSION}

mkdir tf_temporary_folder

cd tensorflow-${TF_VERSION}

TF_SERVING_PROTO=../tf_temporary_folder

python -m grpc.tools.protoc \
    ./tensorflow/core/framework/*.proto \
    --python_out=${TF_SERVING_PROTO} \
    --grpc_python_out=${TF_SERVING_PROTO} \
    --proto_path=.

python -m grpc.tools.protoc \
    ./tensorflow/core/example/*.proto \
    --python_out=${TF_SERVING_PROTO} \
    --grpc_python_out=${TF_SERVING_PROTO} \
    --proto_path=.

python -m grpc.tools.protoc \
    ./tensorflow/core/protobuf/*.proto \
    --python_out=${TF_SERVING_PROTO} \
    --grpc_python_out=${TF_SERVING_PROTO} \
    --proto_path=.

python -m grpc.tools.protoc \
    ./tensorflow_serving/apis/*.proto \
    --python_out=${TF_SERVING_PROTO} \
    --grpc_python_out=${TF_SERVING_PROTO} \
    --proto_path=.

mv LICENSE ..



cd ..

rm -r serving-${TFS_VERSION} tensorflow-${TF_VERSION}
mv tf_temporary_folder/* .

rm -fr tf_temporary_folder

touch tensorflow/__init__.py
touch tensorflow_serving/__init__.py
