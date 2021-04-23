#include <iostream>
#include <chrono>

using namespace std;
using namespace chrono;

bool isPan(string str);

int main() {
	auto start = high_resolution_clock::now();
	long long n = 1;
	long long biggest = 1;
	bool flag = false;
  while (!flag){
		string str = to_string(n);
		for (int i = 2; i < 10; i++){
			str = str + to_string((i * n));
			if (str.length() > 9 &&  i == 2){
				flag = true;
			}
			if (str.length() > 9){
				break;
			}
			if (isPan(str)){
				if (stoll(str) > biggest){
					//cout << endl << biggest << endl;
					biggest = stoll(str);
					break;
				}
			}
		}
		n++;
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<milliseconds>(end - start);
	cout << biggest << endl;
	cout << "Solution found in " << dura.count() << " milliseconds" << endl;
}

bool isPan(string str){
	if (str.length() != 9){
		return false;
	}
	int digi[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
	for (int i = 0; i < str.length(); i++){
		digi[stoi(str.substr(i, 1)) - 1]++;
	}
	for (int i = 0; i < 9; i++){
		if(digi[i] != 1){
			return false;
		}	
	}
	return true;
}
