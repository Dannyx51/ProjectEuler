#include <iostream>
#include <math.h>
#include <vector>
#include <algorithm>
#include <chrono>

using namespace :: std;
using namespace :: chrono;

int getSumFact(int n){
	int sum = 1;
	for (int i = 2; i <= sqrt(n); i++){
		if (n % i == 0){
			sum += i;
			int j = n / i;
			if (j != i){
				sum += j;
			}
		}
	}
	return sum;
}

int main(){
	auto start = high_resolution_clock::now();
	vector<int> abund;
	for (int i = 1; i < 28124; i++){
		if (getSumFact(i) > i){
			abund.push_back(i);
		}
	}
	bool sums[28124];
	for (int i = 0; i < abund.size(); i++){
		for (int j = i; j < abund.size(); j++){
			int n = abund.at(i) + abund.at(j);
			if (n < 28124){
				sums[n] = true;
			} else {
				break;
			}
		}
	}
	int sum = 0;
	for (int i = 1; i < 28124; i++){
		if (!sums[i]){
			sum += i;
		}
	}
	auto end = high_resolution_clock::now();
	auto diff = duration_cast<milliseconds>(end - start);
	cout << sum << endl;
	cout << "Solution took " << diff.count() << " milliseconds to find" << endl;
}
