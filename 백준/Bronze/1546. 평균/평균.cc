#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;

int n, a, maxN;
vi arr;

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> a;
        arr.push_back(a);
    }
    int max = *max_element(arr.begin(), arr.end());
    double temp = 0;
    for (int num : arr)
    {
        temp += (num - 0.0) / (max - 0.0) * 100;
    }
    cout << temp / n;
}