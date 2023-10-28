#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;

int n, cnt = 0, i = 666;
string ans, a;

bool find666(const string &str)
{
    if (str.find("666") != string::npos)
    {
        return true;
    }
    else
    {
        return false;
    }
}

int main()
{
    cin >> n;
    while (cnt != n)
    {
        a = to_string(i);
        if (find666(a))
        {
            cnt++;
        }
        i++;
    }
    cout << a;
}