#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vl;

unordered_map<string, string> h;

vector<string> v;
string name;
vector<vi> graph;

#include <iostream>

long long a[1500050];
int INF = 1000000;

void fibonacci()
{
    a[0] = 0;
    a[1] = 1;
    for (int i = 0; i < 1500000; i++)
    {
        a[i + 2] = (a[i + 1] + a[i]) % INF;
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    long long n;
    std::cin >> n;
    fibonacci();
    std::cout << a[n % 1500000] << "\n";

    return 0;
}