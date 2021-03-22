#include <iostream>

using namespace :: std;

int main() {
  int a;
  int b;
  int c;
  // A < B < C
  // A + B + C = 1000;
  // A^2 + B^2 = C^2

  for (int i = 1; i < 1000; i++){
    for (int ii = 1; ii < 1000; ii++){
      if (i == ii){
        continue;
      }
      a = i;
      b = ii;
      c = 1000 - (a + b);
      if (a > b || c < b || a == b || b == c){
        continue;
      }
      if (a + b + c != 1000){
        continue;
      }
      if ((a * a) + (b * b) == (c * c)){
        cout << a << ", " << b << ", " << c << endl;
        cout << a * b * c << endl;
        return 0;
      }
    }
  }
}
