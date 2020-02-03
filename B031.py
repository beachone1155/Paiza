N = int(input())
S = input()

def henkann():
    for i in range(N): 
        #for文で回すと文字数の違いでうまく行かない。
        #違う文字数のものも同時に変換したい。
        #iじゃなくてn(nは任意の自然数)にしたい
        global S　#global宣言
        S = S.replace("w"+"b"*i+"w","w"+"x"*i+"w").replace("b"+"w"*i+"b","b"+"y"*i+"b")
        S = S.replace("x","w").replace("y","b")
for j in range(N):
    henkann()

#print(S.count("b"))
print(S)