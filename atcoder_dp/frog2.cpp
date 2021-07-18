#include <iostream>
using namespace std;
#include <bits/stdc++.h>
#define init() ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define debug1(x) cout << x << endl;
#define debug2(x, y) cout << x << " " << y << endl;
using ll = long int;


void solve(){

    ll n, k, min_cost;
    cin >> n >> k;
    ll arr[n+1];
    ll costs[n+1] = {0};

    for(ll i=1; i<=n; i++) cin >> arr[i];

    costs[1] = 0;
    for(ll i=2; i<=n; i++){
        min_cost = LONG_MAX;
        for(ll j=1; j<=k; j++){
            if(i - j >= 1) min_cost = min(min_cost, costs[i - j] + abs(arr[i] - arr[i - j]));
        }
        costs[i] = min_cost;
    }

    cout << costs[n] << "\n";

}


int main() {

	init();

	//ll t;
	//cin >> t;
	//while(t--)
	    solve();

	return 0;
}
