## Note for C++ Programs

#### Leetcode Reference
"Compiled with clang 19 using the latest C++ 23 standard, and libstdc++ provided by GCC 14."

#### Installation
```shell
brew install gcc
```

```shell
export GCC_HOME=$(brew --prefix gcc)
export PATH="$PATH:$GCC_HOME/bin"
```

```shell
gcc14 --version
g++14 --version
```

#### Potential Direnv Config for Usage with Cmake
```shell
source_up
export CC="$GCC_HOME/bin/gcc-14"
export CXX="$GCC_HOME/bin/g++-14"
```
