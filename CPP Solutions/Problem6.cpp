#include <iostream>

using namespace :: std;

int main() {
  int sqrF;
  int sqrS;
  int sum = 0;
  for (int i = 1; i <= 100; i++){
    sum += i;
    sqrF += (i * i);
  }
  sqrS = sum * sum;
  //cout << sqrS << endl;
  cout << sqrF - sqrS << endl;
}
