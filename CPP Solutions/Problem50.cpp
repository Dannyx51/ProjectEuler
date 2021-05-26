#include <iostream>
#include <chrono>
#include <vector>
#include "pHelper.h"

using namespace std;
using namespace chrono;

int main() {
	auto start = high_resolution_clock::now();
	int max = 1000000;
  	vector<int> p;
 	p = genPVec(max);
	int len = p.size();
	long sum = 0;
	int l = 0;
	int ind = -1;
	while (sum < max){
		ind++;
		sum += p.at(ind);
		//cout << sum << endl;
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<seconds>(end - start);
	cout << sum - p.at(ind) - 10 << endl;
	cout << "Solution found in " << dura.count() << " seconds" << endl;
}
