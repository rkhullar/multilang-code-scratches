#!/usr/bin/env sh
set -x
here=$(dirname "$(realpath "$0")")
cd "${here}" || exit
rm -rf local/build local/dist

# arch: amd64 | arm64

mkdir -p local/build local/dist
GOOS=linux GOARCH=arm64 go build -tags lambda.norpc -o local/build/bootstrap main.go
cd local/build && zip ../dist/package.zip bootstrap

cd "${here}" || exit
rm -rf local/build
