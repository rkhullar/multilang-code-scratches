SHELL:=/bin/zsh

all: build test clean

build:
	@cat <(echo) header.cpp <(echo) solution.cpp <(echo) test_solution.cpp > generated.cpp
	g++ -std=c++11 -o default generated.cpp

test:
	@./default

clean:
	@rm -rf generated.cpp default
