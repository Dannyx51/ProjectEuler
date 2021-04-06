#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

void swap(string *a, string *b){
	string t = *a;
	*a = *b;
	*b = t;
}

int partition(string arr[], int low, int high){
	string pivot = arr[high];
	int i = (low -1);
	for (int j = low; j < high; j++){
		if (arr[j] <= pivot){
			i++;
			swap(&arr[i], &arr[j]);
		}
	}
	swap(&arr[i + 1], &arr[high]);
	return (i + 1);
}

void quickSort(string arr[], int low, int high){
	if (low < high){
		int pi = partition(arr, low, high);

		quickSort(arr, low, pi - 1);
		quickSort(arr, pi + 1, high);
	}
}

void printArr(string arr[], int size){
	int i;
	for (i = 0; i < size; i++){
		cout << arr[i] << endl;
	}
}

int wordValue(string str, int n){
	int val = 0;
	for (int i = 0; i < str.size(); i++){
		char temp = str.at(i);
		val += (int(temp) - 64);
	}
	val *= n;
	return val;
}

int main() {
	ifstream file;
	string word, t, q;
	file.open("names.txt");
	string shidpant;
	while (file >> word){
		shidpant = word;
	}
	string arr[5163];
	stringstream check1(shidpant);
	string temp;
	int count = 0;
	while(getline(check1, temp, ',')){
		arr[count] = temp.substr(1, temp.size() - 2);
		count++;
	}
	int n = sizeof(arr)/sizeof(arr[0]);
	quickSort(arr, 0, n -1);
	int sum = 0;
	for (int i = 0; i < n; i++){
		sum += wordValue(arr[i], i + 1);
	}
	cout << sum << endl;
}
