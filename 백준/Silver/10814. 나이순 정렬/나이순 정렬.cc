#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

int n, a;
string b;

struct AgeName
{
    int age;
    string name;
};

bool compareAN(const AgeName &a, const AgeName &b)
{
    return a.age < b.age;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n;
    AgeName users[n];
    for (int i = 0; i < n; i++)
    {
        cin >> a >> b;
        users[i] = {a, b};
    }

    stable_sort(users, users + n, compareAN);
    for (AgeName an : users)
    {
        cout << an.age << " " << an.name << "\n";
    }
    return 0;
}