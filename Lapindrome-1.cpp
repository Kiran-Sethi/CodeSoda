#include<iostream>
#include<string>
#include<bits/stdc++.h>
using namespace std;

//pass by reference
//void sortString(string &str)
//{
//	sort(str.begin(),str.end());
//	cout<<str;
//}




int main()
{
   int Test;
   cin>>Test;
   cin.ignore(); 
   string str="";
   int out[Test];
   int count=0,test=Test;
   
   while(Test--)
   {
      
      getline(cin, str);
      
    //   copying in char arr
     
     string::iterator it;
     int len=str.length();
     
     char strs[len];
     int i=0;

     for(it=str.begin();it!=str.end();it++)
      {
          strs[i++]=*it;
     
      }

     ///logic for lapindrome
     
     char firsthalf[len/2];
	 char secondhalf[len/2];
     int beginsecondhalf,endfirsthalf;
     if (len%2==0)
        {
        	beginsecondhalf=len/2;
        	endfirsthalf=len/2;
		}
     else
     	{
     		beginsecondhalf=(len/2) + 1;
			endfirsthalf=len/2 ;
	    }
	   
	    
	 for(int i=0;i<endfirsthalf;i++)
	     firsthalf[i]=strs[i];
	     
	 for(int i=0;i<len/2;i++) 
	     secondhalf[i]=strs[i+beginsecondhalf];
	     
	 int n=sizeof(firsthalf)/sizeof(firsthalf[0]);
	 sort(firsthalf,firsthalf+n);
	 sort(secondhalf,secondhalf+n);    
        
     int isLapindrome=1;
     for (int i=0;i<len/2 ;i++)
         { if(firsthalf[i]!=secondhalf[i])
            {
            	isLapindrome=0;
                break;
			}}
			
     out[count++]= isLapindrome;			
        
     


   }
     for(int i=0;i<test;i++)
     {
     	if (out[i]==0)
	     cout<<"NO"<<"\n";
	   else
	     cout<<"YES"<<"\n";
	 }   
   
   
}
