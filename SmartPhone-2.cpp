#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{   long long int N;
    cin>>N;
    long long int budget[N];
    for (long long int i=0;i<N;i++)
    {
    	cin>>budget[i];
	}
	
	sort(budget,budget+N,greater<long long int>());
	for (long long int i=0;i<N;i++)
    {
    	budget[i]*=(i+1);
	}
	
	cout<<*max_element(budget, budget + N);
	
	return 0;
}
