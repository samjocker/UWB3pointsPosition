def coordinate(r1,r2,r3,circle1=(20,0,24),circle2=(-20,0,24),circle3=(0,-20,5)): #(x,y,z)
    times = True
    i = 0
    AC = abs(circle1[0]-circle2[0])    #AC之間的距離
    AD = ((r1)**2-(r2)**2+AC**2)/(AC*2)     #AD之間的距離
    r4 = ((r1)**2-(AD)**2)**0.5             #r4=BD距離(可能位置的假想圓(假想圓4)半徑)
    if circle1[0] < circle2[0]:             #計算假想圓4的x座標
        circle4_x = circle1[0]+AD
    elif circle1[0] > circle2[0]:
        circle4_x = circle1[0]-AD
    circle4 = (circle4_x, circle1[1], circle2[2])       #假想圓4的座標
    uwb3tocircle4_x = circle4[0]-circle3[0]             #UWB3x座標到假想圓4的x座標距離
    r5 = ((r3)**2-(uwb3tocircle4_x)**2)**0.5            #UWB3的距離做勾股定理抵銷跟假想圓4的斜邊長度差
    circle5 = (circle4_x, circle3[1], circle3[2])
    h = circle4[1]
    k = circle4[2]
    y_start = int(r4)
    for y in range(y_start,0,-1):
        i+=1
        minus_y = y*-1
        may_z1 = (2*k+((4*(k**2)-4*((h**2)+(y**2)-2*y*h+(k**2)-(r4**2)))**0.5))/2
        may_z2 = (2*k-((4*(k**2)-4*((h**2)+(y**2)-2*y*h+(k**2)-(r4**2)))**0.5))/2
        may_minusZ1 = (2*k+((4*(k**2)-4*((h**2)+(minus_y**2)-2*minus_y*h+(k**2)-(r4**2)))**0.5))/2
        may_minusZ2 = (2*k-((4*(k**2)-4*((h**2)+(minus_y**2)-2*minus_y*h+(k**2)-(r4**2)))**0.5))/2
        distance1 = abs((((circle5[1]-y)**2+(circle5[2]-may_z1)**2)**0.5)-r5)
        distance2 = abs((((circle5[1]-y)**2+(circle5[2]-may_z2)**2)**0.5)-r5)
        minus_distance1 = abs((((circle5[1]-minus_y)**2+(circle5[2]-may_minusZ1)**2)**0.5)-r5)
        minus_distance2 = abs((((circle5[1]-minus_y)**2+(circle5[2]-may_minusZ2)**2)**0.5)-r5)
        if times == True:
            last_distance1 = distance1
            last_distance2 = distance2
            last_minusDistance1 = minus_distance1
            last_minusDistance2 = minus_distance2
            last_y = y
            last_minusY = minus_y
            last_mayZ1 = may_z1
            last_mayZ2 = may_z2
            last_mayMinusZ1 = may_minusZ1
            last_mayMinusZ2 = may_minusZ2
        if last_distance1 < distance1 and distance1 < distance2 and distance1 < minus_distance1 and distance1 < minus_distance2:
            target = (circle4[0],last_y,last_mayZ1)
            return target
        elif last_distance2 < distance2 and distance1 > distance2 and distance2 < minus_distance1 and distance2 < minus_distance2:
            target = (circle4[0],last_y,last_mayZ2)
            return target
        elif last_minusDistance1 < minus_distance1 and minus_distance1 < distance1 and minus_distance1 < distance2 and minus_distance1 < minus_distance2:
            target = (circle4[0],last_minusY,last_mayMinusZ1)
            return target
        elif last_minusDistance2 < minus_distance2 and minus_distance2 < distance1 and minus_distance2 < distance2 and minus_distance1 > minus_distance2:
            target = (circle4[0],last_minusY,last_mayMinusZ2)
            return target
        last_distance1 = distance1
        last_distance2 = distance2
        last_minusDistance1 = minus_distance1
        last_minusDistance2 = minus_distance2
        last_mayZ1 = may_z1
        last_mayZ2 = may_z2
        last_mayMinusZ1 = may_minusZ1
        last_mayMinusZ2 = may_minusZ2
        last_y = y
        last_minusY = minus_y
        times = False
import time
start = time.time()
for j in range(10000):  #測試效率
    anser = coordinate(79.30708780180757, 113.84177335182824, 95.30453628824571)
end = time.time()
usetime = end-start
print(anser,usetime)