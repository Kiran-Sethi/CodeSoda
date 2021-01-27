#include <bits/stdc++.h> 
#include<iostream>
#include<vector>
using namespace std;
int main() {
	long long int n, i, t, j, count, max=0;;
	vector<long long int> v;
	cin>>t;
	while(t--) {
		cin>>n;
		count=0;
		for(i=0;i<n;i++){
			cin>>j;
			if(i==0){
				max = j;
				count+=1;
			}else {
				if(j<max){
					count+=1;
					max=j;
				}
			}
		}
		cout<<count<<"\n";
	}
	return 0;
}
