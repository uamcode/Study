import sys 

def limbo(n,heights):
    max_height=160
    
    for i in range(n):
        if heights[i] <= max_height:
            print('I',heights[i])
            return
        
    print('P')
    
n=int(sys.stdin.readline())
heights=list(map(int,sys.stdin.readline().split()))

limbo(n,heights)

# 개 시발롬들 문제 ㅈㄴ 애매하게 쳐내고 기초라고 낄낄 거리네 시발 새긲들 
# 걍 입력 받으라고 하면 되지 왜 n을 써서 쳐 내고 지랄이야 한시간동안 이것만 ㅈㄴ 풀었네 시발
# 후,,근데 간단하게 풀려면 함수로 푸는게 맞구나 넌 아직 멀었다 이 ㅈ 밥년아 
