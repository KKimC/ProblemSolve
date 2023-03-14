n,a = int(input()),"".join(sorted(input().split(), key=lambda x:((x*11)[:11]),reverse=True))
print( a if (a*10)[:10] != "0"*10 else "0")