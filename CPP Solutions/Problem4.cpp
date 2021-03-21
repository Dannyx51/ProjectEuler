#include <iostream>
#include <string>
#include <algorithm>

using namespace :: std;

int main() {
  int biggest = 0;
  for (int i = 100; i < 1000; i++){
    for (int ii = 100; ii < 1000; ii++){
      int num = i * ii;
      string str = to_string(num);
      string rstr = str;
      reverse(str.begin(), str.end());
      if (str == rstr){
        if (num > biggest){
          biggest = num;
        }
      }
    }
  }
  cout << biggest << endl;
}
