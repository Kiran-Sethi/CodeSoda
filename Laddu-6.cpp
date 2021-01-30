#include<iostream>
#include<string>
using namespace std;




int main() 
{ 
    int T,act,rank,sever,orig,para,laddu,maxmonth;
    string origin,activity;

    cin>>T;
    while(T--)
    { laddu=0; 
      cin>>act>>origin;
      if(origin=="INDIAN")
        orig=1;
      else
        orig=2;

      while(act--)
      { cin>>activity;
        if(activity=="CONTEST_WON")
          {cin>>para;
          if(para<=20)
           laddu+=320-para;
          else
           laddu+=300; 
          para=0;}
        if(activity=="TOP_CONTRIBUTOR") 
          laddu+=300;
        if(activity=="BUG_FOUND")  
         {cin>>para;
          laddu+=para;
          para=0;
         } 
        if(activity=="CONTEST_HOSTED") 
          laddu+=50; 
      }  
     if(orig==1)
      maxmonth=laddu/200;
     else
      maxmonth=laddu/400;

     cout<<maxmonth<<"\n"; 
    }
   
    return 0;
}