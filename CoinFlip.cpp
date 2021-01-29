#include <bits/stdc++.h> 
#include<iostream>
#include<vector>
using namespace std;
int main() {
	long long int n, g, q, j, i, t, countH, countT;
	cin>>t;
	while(t--) {
		cin>>g;
		while(g--){
			countH=0;
			countT=0;
			cin >>i>>n>>q;
			if(i==1){
				if(n%2 == 0) {
					countH+= n/2;
					countT = n-countH;
				}else{
					countT+= n/2+1;
					countH = n-countT;
				}
			}else {
				if(n%2 == 0) {
					countT+= n/2;
					countH = n-countT;
				}else{
					countH+= n/2+1;
					countT = n-countH;
				}
			}
			if(q == 1)
				cout<<countH<<"\n";
			else 
				cout<<countT<<"\n";
		}
	}
	return 0;
}
