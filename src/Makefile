CC = gcc
FLAGS = -lm

all: a.out

a.out: test.o reader.o
	$(CC) $^ $(FLAGS)
	
test.o: test.c reader.h
reader.o: reader.c reader.h

clean: $(wildcard *.out *.o)
	rm -f $^