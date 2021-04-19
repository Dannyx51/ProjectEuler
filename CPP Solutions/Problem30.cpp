#include <iostream>
#include <math.h>
#include <vector>
#include <chrono>
using namespace std;
using namespace chrono;
int main() {
	auto start = high_resolution_clock::now();
	int found = 0;
	int n = 2;
	int s = 0;
	int prev = 0;
	int max = 59049;
	while (n < max){
		//cout << n << endl;
		int sum = 0;
		int len = to_string(n).length();
		for (int i = 0; i < len; i++){
			int digi = stoi(to_string(n).substr(i, 1));
			sum += pow(digi, 5);
		}
		if (sum == n){
			//cout << n << endl;
			max = len * 59049;
			found ++;
			s += n;
		}
		n++;
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<milliseconds>(end - start);
	cout << s << endl;
	cout << "Solution found in " << dura.count() << " milliseconds" << endl;
}
