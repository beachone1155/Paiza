t,b,u,d,l,r = map(int,input().split())
n = int(input())
ans = 0

for i in range(n):
    now_t = t
    now_b = b
    now_u = u
    now_d = d
    now_l = l
    now_r = r
    next_box = int(input())
    if next_box == u:
        t = now_u
        u = now_b
        b = now_d
        d = now_t
        ans += 1
    elif next_box == d:
        t = now_d
        d = now_b
        b = now_u
        u = now_t
        ans += 1
    elif next_box == r:
        t = now_r
        r = now_b
        b = now_l
        l = now_t
        ans += 1
    elif next_box == l:
        t = now_l
        l = now_b
        b = now_r
        r = now_t
        ans += 1
    elif next_box == b:
        t = now_b
        b = now_t
        ans += 2

print(ans)