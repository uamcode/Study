def solution(array, commands):
    answer=[]
    for i,j,k in commands:
        array2=array[i-1:j]
        array2.sort()
        answer.append(array2[k-1])
    return answer

# 그냥 너무 어렵게 생각한듯 
# 2차원 배열에서 for i j k in commands 이렇게 쓰는걸 몰라서 
# 딕셔너리로 개고생했네 시발 
    
    

