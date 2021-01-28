#include<iostream>
using namespace std;

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
