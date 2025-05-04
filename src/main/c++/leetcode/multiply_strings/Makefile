SHELL:=/bin/zsh

all: build test clean

build:
	@cat <(echo) header.cpp <(echo) solution.cpp <(echo) test_solution.cpp > generated.cpp
	${CXX} -std=c++23 -o default generated.cpp

test:
	@./default

clean:
	@rm -rf generated.cpp default
