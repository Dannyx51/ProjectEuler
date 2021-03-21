#include <iostream>
#include <chrono>

using namespace :: std;

bool isPrime(int num){
  for (int i = 2; i <= (num/2) + 1; i++){
    if (num % i == 0){
      return false;
    }
  }
  return true;
}

int main() {
  bool found = false;
  int i = 3;
  int numPrimes = 1;
  while(!found){
    if (numPrimes == 10001){
      cout << i - 1 << endl;
      return 0;
    }
    if (isPrime(i)){
      //cout << i << " is prime" << endl;
      numPrimes++;
    }
    i++;
  }
}
