#pragma once

#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>

static unsigned int bins[0xFF];
extern int verbose;

// Maybe: combine readExecutable() and placeDataInBins() into one function
// input: file pointer
// output: dynamic array with file data
int getFileSize(FILE * fptr);
void readExecutable(FILE * fptr, unsigned char * buffer, int bufferlen);
void placeDataInBins(unsigned char * buffer, int bufferlen);
void getEntropy(int bufferlen);