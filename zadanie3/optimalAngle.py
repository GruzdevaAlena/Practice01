import calc


def Angle(d1,d2,h,v_sand,n):
    resultTime = 100
    angle = 0
    for i in range(1,90):
        x = calc.getX(d1, i)
        l1 = calc.getL1(x, d1)
        l2 = calc.getL2(h, x, d2)
        endTime = calc.getAllTime(l1, l2, v_sand, n)
        if(resultTime > endTime):
            resultTime = endTime
            angle = i
    return [angle,resultTime]