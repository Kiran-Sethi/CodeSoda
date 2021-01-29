#include<iostream>
using namespace std;

int main()
{ 
   int t,g,i,q;
   long long int n,heads,tails;
   cin>>t;
   while(t--)
   {
     cin>>g;
     while(g--)
     {
       cin>>i>>n>>q;
       //i=1 head ,i=2 tail
       if(n%2==0)
       {heads=n/2;
        tails=n/2;}

       else
       {if(i==1)
         {tails=n/2 +1;
          heads=n/2;}
        else
         {heads=n/2 +1;
          tails=n/2;} }

        if(q==1)
         cout<<heads<<"\n";
        else
         cout<<tails<<"\n";  

     }
       } 
    return 0;
}