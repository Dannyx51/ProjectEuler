#include <iostream>
#include <chrono>
#include <vector>
#include <algorithm>

using namespace std;
using namespace chrono;

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

int main() {
	//22 * 333 = 4444
	//1 * 4444 = 4444
	auto start = high_resolution_clock::now();
	int sum = 0;
	vector<int> pan;
	for (int i = 10; i < 100; i++){
		for (int ii = 100; ii < 1000; ii++){
			if (isPan(to_string(i) + to_string(ii) + to_string(i * ii))){
				if (find(pan.begin(), pan.end(), i * ii) == pan.end()){
					sum += i * ii;
					//cout << i << " * " << ii << " = " << i * ii << endl;
					pan.push_back(i * ii);
				}
			}
		}
	}
	for (int i = 1; i < 10; i++){
		for (int ii = 1000; ii < 10000; ii++){
			if (isPan(to_string(i) + to_string(ii) + to_string(i * ii))){
				if (find(pan.begin(), pan.end(), i * ii) == pan.end()){
					sum += i * ii;
					//cout << i << " * " << ii << " = " << i * ii << endl;
					pan.push_back(i * ii);
				}
			}
		}
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<milliseconds>(end - start);
	cout << sum << endl;
	cout << "Solution found in " << dura.count() << " milliseconds" << endl;
}
