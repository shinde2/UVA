#include <iostream>
using namespace std;
#include <bits/stdc++.h>
#define init() ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define debug1(x) cout << x << endl;
#define debug2(x, y) cout << x << " " << y << endl;
using ll = int;


void solve(){

    ll n;
    cin >> n;
    ll arr[n];
    ll DP[n] = {0};

    for(ll i=0; i<n; i++) cin >> arr[i];

    DP[0] = 0;
    DP[1] = abs(arr[1] - arr[0]);

    for(ll i=2; i<n; i++) DP[i] = min(DP[i-1]+abs(arr[i] - arr[i-1]), DP[i-2]+abs(arr[i] - arr[i-2]));

    cout << DP[n-1] << "\n";

}


int main() {

	init();

	//ll t;
	//cin >> t;
	//while(t--){
	    solve();
	//}

	return 0;
}
