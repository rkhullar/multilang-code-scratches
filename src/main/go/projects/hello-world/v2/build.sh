#!/usr/bin/env sh
set -x
here=$(dirname "$(realpath "$0")")
cd "${here}" || exit
rm -rf local/build local/dist

mkdir -p local/build local/dist
GOOS=linux GOARCH=arm64 go build -tags lambda.norpc -o local/build/bootstrap lambda_function.go factory.go
cd local/build && zip ../dist/package.zip bootstrap

cd "${here}" || exit
rm -rf local/build
