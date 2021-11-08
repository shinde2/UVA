#include <iostream>
using namespace std;
#include <bits/stdc++.h>
#define init() ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define debug1(x) cout << x << endl;
#define debug2(x, y) cout << x << " " << y << endl;
#define ll long long
int mx = 1e2;
vector<int> st(4 * mx);


int update(int v, int l, int r, int ui, int uv){

    if(l == r) st[v] = uv;
    else{
        int mid = (l + r) / 2;
        if(ui <= mid) update(2 * v, l, mid, ui, uv);
        else update((2 * v) + 1, mid + 1, r, ui, uv);
        st[v] = st[2 * v] + st[(2 * v) + 1];
    }

}


int sum(int v, int l, int r, int li, int ri){

    if(li > ri) return 0;
    else if(li == l and ri == r) return st[v];
    else{
        int mid = (l + r) / 2;
        return (sum(2 * v, l, mid, li, min(ri, mid)) +
                sum((2 * v) + 1, mid + 1, r, max(li, mid + 1), ri));
    }

}


void build(vector<int>& arr, int v, int l, int r){

    if(l == r) st[v] = arr[l];
    else{
        int mid = (l + r) / 2;
        build(arr, 2 * v, l, mid);
        build(arr, (2 * v) + 1, mid + 1, r);
        st[v] = st[2 * v] + st[(2 * v) + 1];
    }

}


void solve(){

    int n, li, ri, ui, uv, sum_q;
    cin >> n >> li >> ri >> ui >> uv;
    vector<int> arr(n);
    for(int i = 0; i < n; i++) cin >> arr[i];

    build(arr, 1, 0, n - 1);

    sum_q = sum(1, 0, n - 1, li, ri);
    cout << sum_q << "\n";

    update(1, 0, n - 1, 2, 3);

    sum_q = sum(1, 0, n - 1, li, ri);
    cout << sum_q << "\n";

}


int main() {

	init();

	//int t;
	//cin >> t;
	//while(t--)
	    solve();

	return 0;
}



