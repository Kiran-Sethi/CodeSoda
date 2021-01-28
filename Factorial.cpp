#include <bits/stdc++.h> 
#include<iostream>
#include<vector>
using namespace std;
int main() {
	long long int n, i, t, count;
	cin>>t;
	while(t--) {
		cin>>n;
		count=0;
		i=5;
		while(i<=n){
			count+=n/i;
			i=i*5;
		}
		cout<<count<<"\n";
	}
	return 0;
}
