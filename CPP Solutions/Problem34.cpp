#include <iostream>
#include <chrono>

using namespace std;
using namespace chrono;

int fact(int n);

int main() {
	auto start = high_resolution_clock::now();
	int s = 0;
	for (int i = 3; i < 2540161; i++){
		string str = to_string(i);
		//cout << str << endl;
		int sum = 0;
		for (int ii = 0; ii < str.length(); ii++){
			sum += fact(stoi(str.substr(ii,1)));
		}
		if (sum == i){
			s += i;
		}
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<seconds>(end - start);
	cout << s << endl;
	cout << "Solution found in " << dura.count() << " seconds" << endl;
}

int fact(int n){
	if (n == 0){
		return 1;
	}
	int p = 1;
	for (int i = 1; i <= n; i++){
		p *= i;
	}
	return p;
}
