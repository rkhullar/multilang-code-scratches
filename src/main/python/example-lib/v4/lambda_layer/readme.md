## Overview

The `lambda_layer` folder is meant for create `package.zip` archives serving as 
lambda layer versions compatible with the python runtime on either `arm64` or `x86_64`
architectures.

## Instructions
1. Review the `docker-compose.yaml` files from this directory and the parent directory. Update the `platform` value
according to the runtime architecture needed.
2. From the parent directory run `docker-compose up`. It should create an `out` directory with the source and binary
distributions.
3. Copy the wheel file into the `lambda_layer/dist` directory.
4. Run `docker-compose up`. The `out` directory should contain `package.zip`.
