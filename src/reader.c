#include "reader.h"

void readExecutable(FILE * fptr) {
    fread(buffer, sizeof (buffer), 1, fptr);

    for (int i = 0; i < 10; ++i) {
        printf("%u\n", buffer[i]);
    }
}

void placeDataInBins() {
    for (int i = 0; i < 0xFF; ++i) bins[i] = 0;
    for (int i = 0; i < 10; ++i) {
        bins[(int)buffer[i]] += 1;
    }

    for (int i = 0; i < 0xFF; ++i) printf("bin %d: %d ocurrences\n", i, bins[i]);
}

// Early implementation of Shannon's entropy. Corroborate
void getEntropy() {
    double entropy = 0;
    for (int i = 0; i < 0xFF; ++i) {
        if (bins[i] == 0) continue;
        double p = 1.0 * bins[i] / 10;
        entropy -= p * log(p) / log(0xFF);
    }

    printf("entropy: %f\n", entropy);
    printf("probability: %Lf\n", probability);
    printf("%f\n", (1.0 / 256));
}