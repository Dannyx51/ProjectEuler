#include <iostream>

using namespace :: std;

int main() {
  long num = 600851475143;
  long temp = num;
  long biggest = 0;

  int i = 2;
  while(i * i <= temp){
    if (temp % i == 0){
      temp = temp / i;
      biggest = i;
    } else {
      i++;
    }
  }
  if (temp > biggest){
    biggest = temp;
  }
  cout << biggest << endl;
}
