#include "reader.h"

// TODO: implement function to get the size of a file. Use to make buffer size dynamic. (done)

int main(int argc, char ** args) {

    if (argc < 2) exit(0); // add help/options function
    char * path = args[1];
    if (argc == 3 && !strncmp(args[2], "-v", 3)) verbose = 1; 
    // else verbose = 0;

    FILE * fptr = fopen(path, "rb");
    if (fptr == NULL) {
        printf("Error: couldn't open file\n");
        exit(1);
    }

    int bufferlen = getFileSize(fptr);

    unsigned char * buffer = (unsigned char *) malloc(sizeof (unsigned char) * bufferlen);
    if (buffer == NULL) {
        printf("Error: couldn't allocate buffer\n");
        exit(1);
    }

    readExecutable(fptr, buffer, bufferlen);
    fclose(fptr);

    placeDataInBins(buffer, bufferlen);
    getEntropy(bufferlen);

    free(buffer);

    return 0;
}
