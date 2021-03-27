#include <iostream>
#include <math.h>

using namespace :: std;

int main(){
	double n = pow(2, 1000);
	string num = to_string(n);
	//cout << num;
	int sum = 0;
	for (int i = 0; i < num.length(); i++){
		if (num.substr(i, 1) != "."){
			sum += stoi(num.substr(i, 1));
		}
	}
	cout << sum;
}
