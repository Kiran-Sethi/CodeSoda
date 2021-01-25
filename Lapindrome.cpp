#include <iostream>
#include<string>
using namespace std;

int main() {
    long long int t, i, a[26], b[26], mid, newV, l=0;
    string s;
    cin>>t;
    while(t--){
    	for(i=0;i<26;i++){
    		a[i]=0;
    		b[i]=0;
		}
    	l=0;
        cin>>s;
        //cout<<s;
        if(s.length()%2 == 0){
            mid = s.length()/2-1;
            newV = s.length()/2;
        }else{
            mid = s.length()/2-1;
            newV = s.length()/2+1;
        }
        for(i = 0;i<=mid;i++)
            a[int(s[i]-97)]++;
        for(i = newV;i<s.length();i++)
            b[int(s[i]-97)]++;
        for(i = 0;i<26;i++){
            if(a[i]!=b[i]){
                cout<<"NO\n";
                l=1;
                break;
            }
        }
        if(l==0)
        	cout<<"YES\n";
    }
	return 0;
}

