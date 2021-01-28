#include<iostream>
using namespace std;

long int count5(int num)
{   long int count=0;
    while (num%5 ==0)
          {count++;
           num/=5;}
    return count;    
}

int main()
{
    long int T;
    long long int N,N_1;
    cin>>T;
    while(T--)
    { cin>>N;
      N_1=N-(N%5);
      long int count=0;
      long int div=5;
      while((N_1/div)>0)
      { 
        count+=N_1/div;
        div*=5;
      
      }
      cout<<count<<"\n"; 

    }
    return 0;
}