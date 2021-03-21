#include <iostream>
#include <chrono>

using namespace :: std;

//Calculates the greatest common divisor by using the Euclidean method
unsigned long long GCD (unsigned long long num1, unsigned long long num2){
  while (num1 != 0){
    unsigned long long num3 = num1;
    num1 = num2 % num1;
    num2 = num3;
  }
  return num2;
}

//lcm calculation
unsigned long long lcm(unsigned long long num1, unsigned long long num2){
  return (num1 * (num2 / GCD(num1, num2)));
}

int main() {
  //NO MORE BRUTE FORCING!!!!!!!!!!!
  auto start = chrono::high_resolution_clock::now();
  bool found = false;
  while (!found){
    unsigned long long result = 1;
    for (unsigned int i = 2; i <= 20; i++){
      result = lcm(result, i);
    }
    auto stop = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
    cout << result << " Ran in " << duration.count() << endl;
    return 0;
  }
}
