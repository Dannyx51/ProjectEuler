#include <iostream>
#include <math.h>

using namespace :: std;

int sumFact(int n){
	//finding factors
	int sum = 0;
	int num = (n / 2) + 1;
	for (int i = 1; i < num; i++){
		if (n % i == 0){
			sum += i;
		}
	}
	return sum;
}


int main() {
	int sum = 0;
	for (int i = 2; i < 10000; i++){
		int a = sumFact(i);
		int b = sumFact(a);
		//cout << i << ": " << sumFact(i) << endl;
		if (i == b && i != a){
			sum += i;
		}
	}
	cout << sum << endl;
}
