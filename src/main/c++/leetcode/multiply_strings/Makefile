SHELL:=/bin/zsh

all: build test clean

build:
	@cat <(echo) header.cpp <(echo) solution.cpp <(echo) test_solution.cpp > generated.cpp
	g++ -o default generated.cpp

test:
	@./default 6

clean:
	@rm -rf generated.cpp default
