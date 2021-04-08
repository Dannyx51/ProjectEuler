#include <iostream>
#include <chrono>
#include <algorithm>

using namespace std;
using namespace chrono;

void printPermu(int arr[], int n){
	cout << "(";
	for (int i = 0; i < n; i++){
		cout << "'" << arr[i] << "' ";
	}
	cout << ")" << endl;
}

void permu(int arr[], int n, int c){
	sort(arr, arr + n);
	do {
		//printPermu(arr, n);
		c++;
		if (c == 1000001){
			printPermu(arr, n);
		}
	} while (next_permutation(arr, arr + n));
}


int main() {
	auto start = high_resolution_clock::now();

	int arr[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
	int n = sizeof(arr) / sizeof(arr[0]);
	int count = 1;
	permu(arr, n, count);

	auto end = high_resolution_clock::now();
	//output ans
	auto dura = duration_cast<microseconds>(end - start);
	cout << "Took " << dura.count() << " microseconds" << endl;
}
