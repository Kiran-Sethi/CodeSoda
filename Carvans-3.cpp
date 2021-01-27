#include<iostream>
#include<bits/stdc++.h>
#include<vector>

using namespace std;
int compare(vector <int> arr1,vector <int>arr2)
{
	int count=0;
	for(int i=0;i<arr1.size();i++)
	 if(arr1[i]==arr2[i]) count++;
	
	return count;
}

int main()
{
	int T,carTot,element;
	cin>>T;
	vector <int> maxSpeed,actualSpeed;
	while(T--)
	{ 
	   cin>>carTot;
	   for (int i=0;i<carTot;i++)
	    {cin>>element;
	     maxSpeed.push_back(element);
	     if(i==0 )
	      actualSpeed.push_back(element);
	     else
		   if(element> actualSpeed[i-1])
		      actualSpeed.push_back(actualSpeed[i-1])  ;
		   else
		      actualSpeed.push_back(element);   
	     } 
	    
//	    for (int i=0;i<carTot;i++) 
//	    cout<<actualSpeed[i]<<"\n";
	    
	    cout<<compare(maxSpeed,actualSpeed)<<"\n";
	    
	    maxSpeed.clear();
		actualSpeed.clear();	
	}
	
	return 0;
}
