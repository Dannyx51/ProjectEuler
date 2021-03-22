#include <iostream>
#include <cmath>

using namespace :: std;

bool isPrime(int num){
  for (int i = 2; i <= sqrt(num); i++){
    if (num % i == 0){
      return false;
    }
  }
  return true;
}
int main() {
  int max = 2000000;
  //starting at 7 beacuse my prime number checker doesn't detect 2 or 5;
  long sum = 7;
  for (int i = 3; i < 2000000; i += 2){
    if (i % 5 == 0){
      continue;
    }
    if (isPrime(i)){
      //cout << i << endl;
      sum += i;
    }
  }
  cout << sum;
}
