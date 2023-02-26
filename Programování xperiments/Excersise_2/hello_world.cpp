#include <iostream>
#include <string>
#include <cstdlib>

int main(int argc, char* argv[]) {
  if (argc != 2) {
    std::cerr << "Usage: " << argv[0] << " <number>" << std::endl;
    return 1;
  }

  int input_number = std::atoi(argv[1]);
  std::cout << "Hello world " << input_number << std::endl;

  return 0;
}
