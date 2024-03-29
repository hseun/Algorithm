def solution(myStr):
    myStr = [x for x in myStr.replace("a", " ").replace("b", " ").replace("c", " ").split()]
    return myStr if myStr else ["EMPTY"]