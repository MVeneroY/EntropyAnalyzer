#include "reader.h"

int getFileSize(FILE * fptr) {
    fseek(fptr, 0, SEEK_END);
    int size = ftell(fptr);
    fseek(fptr, 0, SEEK_SET);

    return size;
}

void readExecutable(FILE * fptr, unsigned char * buffer, int bufferlen) {
    printf("Size of file: %d bytes\n", bufferlen);
    fread(buffer, bufferlen, 1, fptr);
}

void placeDataInBins(unsigned char * buffer, int bufferlen) {
    for (int i = 0; i < 0xFF; ++i) bins[i] = 0;
    for (int i = 0; i < bufferlen; ++i) {
        bins[(int)buffer[i]] += 1;
    }
}

// Early implementation of Shannon's entropy. Corroborate
void getEntropy(int bufferlen) {
    double entropy = 0;
    for (int i = 0; i < 0xFF; ++i) {
        if (bins[i] == 0) continue;
        double p = 1.0 * bins[i] / bufferlen;
        entropy -= p * log(p) / log(0xFF);
    }

    printf("entropy: %f\n", entropy);
}