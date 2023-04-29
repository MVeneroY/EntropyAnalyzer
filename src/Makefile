CC = gcc
FLAGS = -lm
TARGET=../target

all: entropy

entropy: test.o reader.o
	mkdir -p $(TARGET)
	$(CC) $^ $(FLAGS) -o $(TARGET)/entropy
	
test.o: test.c reader.h
reader.o: reader.c reader.h	

clean:
	rm -f $(wildcard *.out *.o $(TARGET)/entropy)