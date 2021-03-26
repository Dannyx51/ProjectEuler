#include <iostream>

using namespace :: std;

int main() {
	int n = 50;
	unsigned long long arr[n][n];
    	for (int line = 0; line < n; line++){
        	for (int i = 0; i <= line; i++){
			if (line == i || i == 0){
				arr[line][i] = 1;
			} else {
				arr[line][i] = arr[line - 1][i - 1] +arr[line - 1][i];
			}
		}
    	}
	long b = 0;
	for (int i = 0; i < n; i++){
		//array rows with odd number of columns have answers
		if (i % 2 == 0 && i == 40){
			for (int ii = 0; ii <= i; ii++){
				if (arr[i][ii] > b){
					b = arr[i][ii];
				}	
			}
		}
	}
	cout << b;
	//cout << arr[s * 2][sizeof(arr[] / 2)]
}
