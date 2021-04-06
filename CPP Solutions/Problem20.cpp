#include <iostream>

using namespace :: std;

// "Kashoot!" me
// give me BigInteger pls
int mult(int n, int arr[], int s){
	int r = 0;
	for (int i = 0; i < s; i++){
		int num = arr[i] * n + r;
		arr[i] = num % 10;
		r = num / 10;
	}
	while (r){
		arr[s] = r % 10;
		r = r/10;
		s++;
	}
	return s;
}

int main() {
	int n = 100;
  int digi[158];
	digi[0] = 1;
	int s = 1;
	for (int i = 2; i <= n; i++){
		s = mult(i, digi, s);
	}
	int sum = 0;
	for(int i = s - 1; i >= 0; i--){
		sum += digi[i];
	}
	cout << sum << endl;
}
