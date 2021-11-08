#include <iostream>
using namespace std;
#include <bits/stdc++.h>
#define init() ios::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define debug1(x) cout << x << endl;
#define debug2(x, y) cout << x << " " << y << endl;
#define ll long long
int mx = 1e2;
vector<int> st(4 * mx);
vector<bool> marked(4 * mx);


void push(int v){

    st[2 * V] = st[v];
    st[2 * v + 1] = st[v];
    marked[2 * v] = true;
    marked[2 * v + 1] = true;
    marked[v] = false;
}


int update(int v, int l, int r, int ul, int ur, int uv){

    if(l == ul and r == ur){
        st[v] = uv;
        marked[v] = true;
    }
    else{
        push(v)
        int mid = (l + r) / 2;
        update(2 * v, l, mid, ul, min(mid, r), uv);
        update((2 * v) + 1, mid + 1, max(mid + 1, l), r, uv);
    }

}


int get(int v, int l, int r, int pos){

    if(marked[v]) return st[v];
    else{
        int mid = (l + r) / 2;
        if(pos <= mid) return get(2 * v, l, mid, pos);
        else return get(2 * v + 1, mid + 1, r, pos);
    }

}


void build(vector<int>& arr, int v, int l, int r){

    if(l == r){
        st[v] = arr[l];
        marked[v] = true;
    }
    else{
        int mid = (l + r) / 2;
        build(arr, 2 * v, l, mid);
        build(arr, (2 * v) + 1, mid + 1, r);
        st[v] = -1;
        marked[v] = false;
    }

}


void solve(){

    /*
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
    */

}


int main() {

	init();

	//int t;
	//cin >> t;
	//while(t--)
	    solve();

	return 0;
}



