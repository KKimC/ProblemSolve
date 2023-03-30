
def turn_left(arr):
    new_arr = [arr[6],arr[3],arr[0],arr[7],arr[4],arr[1],arr[8],arr[5],arr[2]]
    return new_arr

def turn_right(arr):
    new_arr = [arr[2],arr[5],arr[8],arr[1],arr[4],arr[7],arr[0],arr[3],arr[6]]
    return new_arr

def turn_u_p():
    global u
    temp = [f[0],f[1],f[2]]
    f[0],f[1],f[2] = r[6],r[3],r[0]
    r[6],r[3],r[0] = b[8],b[7],b[6]
    b[6],b[7],b[8] = l[8],l[5],l[2]
    l[2],l[5],l[8] = temp[0],temp[1],temp[2]
    u = turn_left(u)

def turn_u_m():
    global u
    temp = [f[0],f[1],f[2]]
    f[0],f[1],f[2] = l[2],l[5],l[8]
    l[2],l[5],l[8] = b[8],b[7],b[6]
    b[6],b[7],b[8] = r[0],r[3],r[6]
    r[6],r[3],r[0] = temp[0],temp[1],temp[2]
    u = turn_right(u)

def turn_d_p():
    global d
    temp = [f[6],f[7],f[8]]
    f[6],f[7],f[8] = l[0],l[3],l[6]
    l[0],l[3],l[6] = b[2],b[1],b[0]
    b[0],b[1],b[2] = r[2],r[5],r[8]
    r[8],r[5],r[2] = temp[0],temp[1],temp[2]
    d = turn_left(d)

def turn_d_m():
    global d
    temp = [f[6],f[7],f[8]]
    f[6],f[7],f[8] = r[8],r[5],r[2]
    r[2],r[5],r[8] = b[0],b[1],b[2]
    b[0],b[1],b[2] = l[6],l[3],l[0]
    l[0],l[3],l[6] = temp[0],temp[1],temp[2]
    d = turn_right(d)

def turn_f_p():
    global f
    temp = [u[6],u[7],u[8]]
    u[6],u[7],u[8] = l[6],l[7],l[8]
    l[6],l[7],l[8] = d[6],d[7],d[8]
    d[6],d[7],d[8] = r[6],r[7],r[8]
    r[6],r[7],r[8] = temp[0],temp[1],temp[2]
    f = turn_left(f)

def turn_f_m():
    global f
    temp = [u[6],u[7],u[8]]
    u[6],u[7],u[8] = r[6],r[7],r[8]
    r[6],r[7],r[8] = d[6],d[7],d[8]
    d[6],d[7],d[8] = l[6],l[7],l[8]
    l[6],l[7],l[8] = temp[0],temp[1],temp[2]
    f = turn_right(f)

def turn_b_p():
    global b
    temp = [u[0],u[1],u[2]]
    u[0],u[1],u[2] = r[0],r[1],r[2]
    r[0],r[1],r[2] = d[0],d[1],d[2]
    d[0],d[1],d[2] = l[0],l[1],l[2]
    l[0],l[1],l[2] = temp[0],temp[1],temp[2]
    b = turn_left(b)

def turn_b_m():
    global b
    temp = [u[0],u[1],u[2]]
    u[0],u[1],u[2] = l[0],l[1],l[2]
    l[0],l[1],l[2] = d[0],d[1],d[2]
    d[0],d[1],d[2] = r[0],r[1],r[2]
    r[0],r[1],r[2] = temp[0],temp[1],temp[2]
    b = turn_right(b)

def turn_l_p():
    global l
    temp = [u[0],u[3],u[6]]
    u[0],u[3],u[6] = b[0],b[3],b[6]
    b[0],b[3],b[6] = d[8],d[5],d[2]
    d[8],d[5],d[2] = f[0],f[3],f[6]
    f[0],f[3],f[6] = temp[0],temp[1],temp[2]
    l = turn_left(l)

def turn_l_m():
    global l
    temp = [u[0],u[3],u[6]]
    u[0],u[3],u[6] = f[0],f[3],f[6]
    f[0],f[3],f[6] = d[8],d[5],d[2]
    d[8],d[5],d[2] = b[0],b[3],b[6]
    b[0],b[3],b[6] = temp[0],temp[1],temp[2]
    l = turn_right(l)

def turn_r_p():
    global r
    temp = [u[2],u[5],u[8]]
    u[2],u[5],u[8] = f[2],f[5],f[8]
    f[2],f[5],f[8] = d[6],d[3],d[0]
    d[6],d[3],d[0] = b[2],b[5],b[8]
    b[2],b[5],b[8] = temp[0],temp[1],temp[2]
    r = turn_left(r)

def turn_r_m():
    global r
    temp = [u[2],u[5],u[8]]
    u[2],u[5],u[8] = b[2],b[5],b[8]
    b[2],b[5],b[8] = d[6],d[3],d[0]
    d[6],d[3],d[0] = f[2],f[5],f[8]
    f[2],f[5],f[8] = temp[0],temp[1],temp[2]
    r = turn_right(r)

move = {"U+":turn_u_p,"U-":turn_u_m,"D+":turn_d_p,"D-":turn_d_m,"F+":turn_f_p,"F-":turn_f_m,"B+":turn_b_p,"B-":turn_b_m,"L+":turn_l_p,"L-":turn_l_m,"R+":turn_r_p,"R-":turn_r_m}
for t in range(int(input())):
    input()
    u = ['w'] * 9
    # u = [1,2,3,4,5,6,7,8,9]
    d = ['y'] * 9
    f = ['r'] * 9
    # f = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = ['o'] * 9
    l = ['g'] * 9
    r = ['b'] * 9
    for j in input().split():
        move[j]()
    print(f'{u[0]}{u[1]}{u[2]}\n{u[3]}{u[4]}{u[5]}\n{u[6]}{u[7]}{u[8]}')
