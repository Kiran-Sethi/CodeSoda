#include <bits/stdc++.h> 
#include<iostream>
#include<vector>
using namespace std;
int main() {
	long long int n, m, i, max = 0;
	vector<long long int> v;
	cin>>n;
	for(i=0;i<n;i++){
		cin>>m;
		v.push_back(m);
		//cout<<"v"<<v[i];
	}
	sort(v.begin(), v.end());
	for(i =0;i<n;i++){
		v[i]= v[i]*(n-i);
		if(v[i]>max)
			max = v[i];
	}
	cout<< max;
	return 0;
}
