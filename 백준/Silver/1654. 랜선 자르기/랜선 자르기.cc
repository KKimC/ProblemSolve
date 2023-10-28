#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;

ll n, a, k, temp;
vi arr;

int main()
{
    int K, N;
    cin >> K >> N;
    vector<ll> vec;

    for (int i = 0; i < K; i++)
    {
        ll length;
        cin >> length;

        vec.push_back(length);
    }
    ll min = *min_element(vec.begin(), vec.end());

    ll left = 1;
    ll right = *max_element(vec.begin(), vec.end());

    ll result = 0;

    while (left <= right)
    {
        ll mid = (left + right) / 2;
        ll sum = 0;
        for (int i = 0; i < K; i++)
        {
            sum += (vec[i] / mid);
        }

        if (sum >= N)
        {
            result = mid;
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }

    cout << result;

    return 0;
}