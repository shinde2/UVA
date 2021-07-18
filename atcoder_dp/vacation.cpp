#include <iostream>
using namespace std;
#include <bits/stdc++.h>
#define init() ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define debug1(x) cout << x << endl;
#define debug2(x, y) cout << x << " " << y << endl;
using ll = long int;


void solve(){

    ll n, mx;
    cin >> n;

    ll DP[n][3];

    for(ll i=0; i<n; i++) cin >> DP[i][0] >> DP[i][1] >> DP[i][2];

    for(ll i=1; i<n; i++){
        for(ll j=0; j<3; j++){
            mx = LONG_MIN;
            for(ll k=0; k<3; k++){
                if(j != k){
                    mx = max(mx, DP[i-1][k]);
                }
            }
            DP[i][j] += mx;
        }
    }

    cout << max(DP[n-1][0], max(DP[n-1][1], DP[n-1][2])) << "\n";

}


int main() {

	init();

	//ll t;
	//cin >> t;
	//while(t--)
	    solve();

	return 0;
}
