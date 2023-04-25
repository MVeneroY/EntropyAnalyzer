#include <stdio.h>
#include <stdlib.h>

#include "reader.h"

// TODO: implement function to get the size of a file. Use to make buffer size dynamic.

int main(int argc, char ** args) {

    if (argc < 2) exit(0); // add help/options function
    char * path = args[1];
    FILE * fptr = fopen(path, "rb");
    if (fptr == NULL) {
        printf("Error: couldn't open file\n");
        exit(1);
    }
    readExecutable(fptr);
    fclose(fptr);

    placeDataInBins();
    getEntropy();

    return 0;
}