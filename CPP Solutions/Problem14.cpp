#include <iostream>
#include <map>

using namespace std;

int main() {
    long int cur = 0;
    int hlen = 0;
    int hnum = 0;
    map<int,int> found;
    for(int i = 2; i < 1000000; i++){
        cur = i;
        int clen = 0;
        while(cur != 1){
            if(found.count(cur)){clen += found.at(cur);break;}
            if(cur % 2 == 0){cur /= 2;}
            else{cur *= 3; cur++;}
            if(cur < 0){cout << cur << " " << clen << endl;return 0;}
            clen++;
        }
        found.insert(pair<int,int>(i,clen));
        if(clen > hlen){hlen = clen; hnum = i;}
    }
    cout << hlen << " " << hnum << endl;
}
