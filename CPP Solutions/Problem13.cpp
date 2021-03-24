#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace :: std;

int main() {
  string line;
  ifstream file("num.txt");
  int num[100][50];
  int counter = 0;
  if (file.is_open()){
    while (getline(file, line)){
      int i = 0;
      //string arr[50];
      while (i < line.length()){
        num[counter][i] = stoi(line.substr(i, 1));
        i++;
      }
      counter++;
    }
    file.close();
  }
  int remainder = 0;
  vector<int> digits;
  for (int col = 49; col >= 0; col--){
    int sum = 0;
    for (int row = 0; row < 100; row++){
      sum += num[row][col];
    }
    sum += remainder;
    string temp = to_string(sum);
    int digi = stoi(temp.substr(temp.length() - 1, 1));
    remainder = stoi(temp.substr(0, temp.length() - 1));
    digits.insert(digits.begin() + 0, digi);
  }
  digits.insert(digits.begin() + 0, remainder);
  string full = "";
  for (int i = 0; i < digits.size(); i++){
    full += to_string(digits.at(i));
  }
  cout << full.substr(0, 10);
}
