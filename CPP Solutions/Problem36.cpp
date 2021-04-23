#include <iostream>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace chrono;

string toBin(int n);
bool isPal(string str);

int main() {
	auto start = high_resolution_clock::now();
	int sum = 0;
  for (int i = 0; i < 1000000; i++){
		if (isPal(to_string(i)) && isPal(toBin(i))){
			sum += i;
		}
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<milliseconds>(end - start);
	cout << sum << endl;
	cout << "Solution found in " << dura.count() << " milliseconds" << endl;
}

bool isPal(string str){
	string tstr = str;
	reverse(str.begin(), str.end());
	if (tstr == str){
		return true;
	}
	return false;
}

string toBin(int n){
	string bin = "";
	while (n > 0){
		bin = to_string(n % 2) + bin;
		n = n / 2;
	}
	return bin;
}
