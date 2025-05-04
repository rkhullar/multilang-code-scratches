#!/usr/bin/env sh

here=$(dirname "$(realpath "$0")")
target_path="${here}/../"
cd "${target_path}" || exit
. venv/bin/activate

set -x
cd "${target_path}/protos" || exit
rm -rf generated && mkdir generated
python -m grpc_tools.protoc -I. --python_out=generated --grpc_python_out=generated --pyi_out=generated ./*.proto
