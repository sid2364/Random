def foo(arr):
    bestmax=0
    bestmaxactual=0
    bestmaxcon=0
    for ele in arr:
        ele=int(ele)
        if ele+bestmax > 0:
            bestmax=ele+bestmax
        elif ele+bestmax < bestmax:
            bestmax=0
        if ele+bestmaxcon > bestmaxcon:
            bestmaxcon=ele+bestmaxcon
        if bestmax > bestmaxactual:
            bestmaxactual=bestmax
    print (max(arr) if bestmaxactual==0 else bestmaxactual, max(arr) if bestmaxcon==0 else bestmaxcon)
inp=int(input())
arr=[]
while inp!=0:
    blu=int(input())
    n=input()
    foo(n.split())
    inp-=1
