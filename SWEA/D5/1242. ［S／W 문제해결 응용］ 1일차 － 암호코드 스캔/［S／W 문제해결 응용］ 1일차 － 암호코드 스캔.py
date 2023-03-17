bins = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
octs = {"211":"0", "221":"1", "122":"2","411":"3","132":"4","231":"5","114":"6","312":"7","213":"8","112":"9"}


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def gcd3(a,b,c):
    return gcd(gcd(a,b),c)


def binss(hexs,cnt):
    #todo 16진수를 56의 배수 길이를 가진 2진수 문자로 변환
    result = ""
    for i in hexs:
        result += bins[i]
    return result.strip("0").zfill(56*cnt)

def make_oct(nums):
    #todo 7자리 암호 이진법 숫자를 10진수 정수로 변환
    lst = [0,0,0]
    last = "1"
    cnt = 0
    for i in nums.rstrip("0"):
        if i == last:
            lst[cnt]+= 1
        else:
            last = i
            cnt += 1
            lst[cnt]+=1
    return octs["".join(map(lambda x: str(x//gcd3(*lst)),lst))]


def bin_to_oct(bins):
    #todo 2진수를 7의 배수개로 잘라서 8자리 10진법 정수로 변환
    bn = len(bins)//56*7
    octss = ''
    for i in range(8):
        strs = bins[i*bn:i*bn+bn]
        result = ''
        for idx,val in enumerate(strs):
            if idx%(len(bins)//56) == 0:
                result += val
        octss += make_oct(result)
    return octss


def check(nums):
    #todo 비밀번호 맞는지 확인
    num_lst = list(map(int,nums))
    if ((num_lst[0]+num_lst[2]+num_lst[4]+num_lst[6])*3 +num_lst[1]+num_lst[3]+num_lst[5]+num_lst[7])%10 == 0:
        return True
    else:
        return False

def cal_result(nums):
    #todo 마지막 결과값 확인
    result = 0
    for i in nums:
        result += int(i)
    return result



for t in range(1,int(input())+1):
    graphs = set()
    anss = set()
    n,m = map(int,input().split())
    bars = [input() for i in range(n)]
    bars = list(set(bars))
    binary_code = ''
    ans = 0
    for i in range(len(bars)):
        arr = bars[i]
        for j in range(m):
            if arr[j] != '0' or arr[len(arr)-i-1] != '0':
                binary_code = ''
                for k in range(m):
                    binary_code += bins[arr[k]]
                binary_code = binary_code.strip('0')
        cnt = 0
        last = "0"
        des = ''
        bresult = ''
        if binary_code:
            for j in binary_code[::-1]:
                if last == "1" and j == "0":
                    cnt += 1
                    if cnt == 2:
                        cnt = 0
                        des += make_oct(bresult[::-1])
                        bresult = ''
                        last = "0"
                    else:
                        last = "0"
                        bresult += j
                else:
                    bresult += j
                    last = j
            des += make_oct(bresult[::-1])
        for i in range(len(des)//8):
            dess = des[i*8:i*8+8][::-1]
            if dess not in anss and check(dess):
                ans += cal_result(dess)
                anss.add(dess)
    print(f"#{t} {ans}")