#include <iostream>
#include <cstring>

void vulnerableFunction(char *input) {
    char buffer[10];  // Small buffer
    strcpy(buffer, input);  // No bounds checking
    std::cout << "You entered: " << buffer << std::endl;
}

int main(int argc, char *argv[]) {
    if (argc > 1) {
        vulnerableFunction(argv[1]);
    } else {
        std::cout << "Usage: " << argv[0] << " <input>" << std::endl;
    }
    return 0;
}
