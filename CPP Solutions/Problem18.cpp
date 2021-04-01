#include <iostream>
#include <vector>

using namespace :: std;

int main() {
  int py[15][15] = {{75},
	{95, 64},
	{17, 47, 82},
	{18, 35, 87, 10},
	{20,  4, 82, 47, 65},
	{19,  1, 23, 75,  3, 34},
	{88,  2, 77, 73,  7, 63, 67},
	{99, 65,  4, 28,  6, 16, 70, 92},
	{41, 41, 26, 56, 83, 40, 80, 70, 33},
	{41, 48, 72, 33, 47, 32, 37, 16, 94, 29},
	{53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14},
	{70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57},
	{91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48},
	{63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31},
	{ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23}};
	
	int moves[15] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	//printMoves(moves);
	
	for (int y = 14; y >= 0; y--){
		if (y != 0){
			for (int x = 0; x < y; x++){
				int num1 = py[y-1][x];
				int num2 = py[y-1][x+1];
				int biggest = 0;
				if (num1 > num2){
					biggest = num1;
				} else {
					biggest = num2;
				}
				int num = py[y][x] + biggest;
				cout << py[y][x] << ": Num1 = " << num1 << " and Num2 = " << num2 << " Biggest: " << biggest << " Output: " << num << endl;
				py[y-1][x] = num;
				//printTri(py);
			}
			cout << endl;
		} else {
			cout << py[0][0] << endl;
		}
	}
}

//1074
