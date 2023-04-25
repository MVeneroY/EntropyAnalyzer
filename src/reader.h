#pragma once

#include <stdio.h>
#include <math.h>

static unsigned char buffer[10];
static unsigned int bins[0xFF];
static const long double probability = 1.0 / 0xFF;
static const double E = 2.718281828459045;

void readExecutable(FILE * fptr);
void placeDataInBins();
void getEntropy();