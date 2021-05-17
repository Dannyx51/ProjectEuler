#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <chrono>

using namespace std;
using namespace chrono;

vector<int> genTri(int n);

int main() {
	auto start = high_resolution_clock::now();
	//Generating triangle numbers
  	vector<int> vecTri = genTri(192); // After testing for the largest wSum i got 192
	// Opening and reading file
  	string word;
	ifstream file;
	file.open("words.txt");
	string str;
	while (file >> word){
		str = word;
	}
	vector<string> words;
	stringstream check1(str);
	string t;
	while (getline(check1, t, ',')){
		words.push_back(t.substr(1, t.size() - 2));
	}
	int tC = 0;
	//Looping through word
	for (int i = 0; i < words.size(); i++){
		//Looping through characters
		string w = words.at(i);
		int wSum = 0;
		for (int ii = 0; ii < w.length(); ii++){
			wSum += w[ii] - 64;
		}
		if (find(vecTri.begin(), vecTri.end(), wSum) != vecTri.end()){
			tC++;
		}
	}
	auto end = high_resolution_clock::now();
	auto dura = duration_cast<milliseconds>(end - start);
	cout << tC << endl;
	cout << "Solution found in " << dura.count() << " milliseconds" << endl;
}

vector<int> genTri(int n){
	vector<int> vec;
	int i = 1;
	int prod = 0;
	while (prod <= n){
		prod = (.5 * i) * (i + 1);
		vec.push_back(prod);
		i++;
	}
	return vec;
}
