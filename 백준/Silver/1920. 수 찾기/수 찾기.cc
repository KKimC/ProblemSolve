#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

int n, m;
ll a;
ll arr[100001];

int bsearch(ll *arr, int s, ll num)
{

    int left = 0, right = s - 1;

    while (left <= right)
    {
        int mid = left + (right - left) / 2;

        if (arr[mid] == num)
        {
            cout << 1 << "\n";
            return mid;
        }
        else if (arr[mid] < num)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    cout << 0 << "\n";
    return -1;
}
int num;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> a;
        arr[i] = a;
    }
    cin >> m;

    sort(arr, arr + n);

    for (int i = 0; i < m; i++)
    {
        cin >> num;
        bsearch(arr, n, num);
    }
}