#include <iostream>
#include <array>

using namespace :: std;

int main() {
  int num1, num2, num3;
  num3 = 0;
  num1 = num2 = 1;

  int max = 4000000;
  int sum = 0;
  while (num3 < max){
    num3 = num1 + num2;
    num1 = num2;
    num2 = num3;
    if (num3 % 2 == 0){
      sum += num3;
    }
  }
  cout << sum;
}
