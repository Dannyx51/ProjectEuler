#include <iostream>
#include <algorithm>
#include <iomanip>
#include <chrono>

using namespace std;
using namespace chrono;

void permu(string arr[], int n, int c);
bool checkRule(string arr[]);

int main() {
	auto start = high_resolution_clock::now();
	string arr[10] = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
	int n = 10;
	int c = 1;
	permu(arr, n, c);
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<seconds>(end - start);
	cout << "Solution found in " << dura.count() << " seconds" << endl;
}

void permu(string arr[], int n, int c){
	sort(arr, arr + n);
	double sum = 0;
	do {
		if (checkRule(arr)){
			string tot = "";
			for (int i = 0; i < 10; i++){
				tot += arr[i];
			}
			sum += stod(tot);
		}
		c++;
	} while (next_permutation(arr, arr + n));
	//cout << c << endl;
	cout << setprecision(12) << sum << endl;
}

bool checkRule(string arr[]){
	if (stoi(arr[1] + arr[2] + arr[3]) % 2 != 0){
		return false;
	} else if (stoi(arr[2] + arr[3] + arr[4]) % 3 != 0){
		return false;
	} else if (stoi(arr[3] + arr[4] + arr[5]) % 5 != 0){
		return false;
	} else if (stoi(arr[4] + arr[5] + arr[6]) % 7 != 0){
		return false;
	} else if (stoi(arr[5] + arr[6] + arr[7]) % 11 != 0){
		return false;
	} else if (stoi(arr[6] + arr[7] + arr[8]) % 13 != 0){
		return false;
	} else if (stoi(arr[7] + arr[8] + arr[9]) % 17 != 0){
		return false;
	}
	return true;
}
