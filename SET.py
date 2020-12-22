import numpy as np

def findSET(p1, p2, p3):
    p1p2 = edgeSET(p1, p2)
    p1p3 = edgeSET(p1, p3)
    p2p3 = edgeSET(p2, p3)

    p1p2_ymin = p1p2.getAttributes()[0]
    p1p2_ymax = p1p2.getAttributes()[1]
    p1p2_xofymin = p1p2.getAttributes()[2]
    p1p2_dx = p1p2.getAttributes()[3]
    p1p2_dy = p1p2.getAttributes()[4]
    p1p2_dxdy = p1p2_dx / p1p2_dy

    p1p3_ymin = p1p3.getAttributes()[0]
    p1p3_ymax = p1p3.getAttributes()[1]
    p1p3_xofymin = p1p3.getAttributes()[2]
    p1p3_dx = p1p3.getAttributes()[3]
    p1p3_dy = p1p3.getAttributes()[4]
    p1p3_dxdy = p1p3_dx / p1p3_dy

    p2p3_ymin = p2p3.getAttributes()[0]
    p2p3_ymax = p2p3.getAttributes()[1]
    p2p3_xofymin = p2p3.getAttributes()[2]
    p2p3_dx = p2p3.getAttributes()[3]
    p2p3_dy = p2p3.getAttributes()[4]
    p2p3_dxdy = p2p3_dx / p2p3_dy

    g_ymin = min(p1p2_ymin, p1p3_ymin, p2p3_ymin)
    g_ymax = max(p1p2_ymax, p1p3_ymax, p2p3_ymax)
    
    yrange = g_ymax - g_ymin
    SET = []
    
    i = g_ymin
    while(i <= yrange):
        SET.append([])
        i += 1
    
    i = p1p2_ymin
    while(i <= p1p2_ymax):
        SET[i].append([p1p2_xofymin, p1p2_dxdy, "p1p2", p1p2_ymin])
        i += 1

    i = p1p3_ymin
    while(i <= p1p3_ymax):
        SET[i].append([p1p3_xofymin, p1p3_dxdy, "p1p3", p1p3_ymin])
        i += 1

    i = p2p3_ymin
    while(i <= p2p3_ymax):
        SET[i].append([p2p3_xofymin, p2p3_dxdy, "p2p3", p2p3_ymin])
        i += 1

    y = g_ymin
    res = []
    while(y <= g_ymax):
        xlist = []
        idx = 0
        ye = SET[y]
        while(idx < len(ye)):
            e = ye[idx]
            if(y == e[3]):
                xlist.append(e[0])

            else:
                holder = 0
                if(e[2] == "p1p2"):
                    holder = p1p2.getHolder()
                elif(e[2] == "p1p3"):
                    holder = p1p3.getHolder()
                elif(e[2] == "p2p3"):
                    holder = p2p3.getHolder()

                e[0] = holder + e[1]
                
                if(e[2] == "p1p2"):
                    p1p2.updateHolder(e[0])
                elif(e[2] == "p1p3"):
                    p1p3.updateHolder(e[0])
                elif(e[2] == "p2p3"):
                    p2p3.updateHolder(e[0])

                e[0] = round(e[0])
                xlist.append(e[0])
            idx += 1
        xmin = min(xlist)
        xmax = max(xlist)
        res.append([y, xmin, xmax])
        y += 1
    
    return res

def findGouraudSET(p1, p2, p3, I1, I2, I3):
    p1p2 = edgeSET(p1, p2)
    p1p3 = edgeSET(p1, p3)
    p2p3 = edgeSET(p2, p3)

    p1p2_ymin = p1p2.getAttributes()[0]
    p1p2_ymax = p1p2.getAttributes()[1]
    p1p2_xofymin = p1p2.getAttributes()[2]
    p1p2_dx = p1p2.getAttributes()[3]
    p1p2_dy = p1p2.getAttributes()[4]
    p1p2_dxdy = 0
    if(p1p2_dx == 0 or p1p2_dy == 0):
        p1p2_dxdy = 0
    else:
        p1p2_dxdy = p1p2_dx / p1p2_dy

    p1p3_ymin = p1p3.getAttributes()[0]
    p1p3_ymax = p1p3.getAttributes()[1]
    p1p3_xofymin = p1p3.getAttributes()[2]
    p1p3_dx = p1p3.getAttributes()[3]
    p1p3_dy = p1p3.getAttributes()[4]
    p1p3_dxdy = 0
    if(p1p3_dx == 0 or p1p3_dy == 0):
        p1p3_dxdy = 0
    else:
        p1p3_dxdy = p1p3_dx / p1p3_dy

    p2p3_ymin = p2p3.getAttributes()[0]
    p2p3_ymax = p2p3.getAttributes()[1]
    p2p3_xofymin = p2p3.getAttributes()[2]
    p2p3_dx = p2p3.getAttributes()[3]
    p2p3_dy = p2p3.getAttributes()[4]
    p2p3_dxdy = 0
    if(p2p3_dx == 0 or p2p3_dy == 0):
        p2p3_dxdy = 0
    else:
        p2p3_dxdy = p2p3_dx / p2p3_dy

    g_ymin = min(p1p2_ymin, p1p3_ymin, p2p3_ymin)
    g_ymax = max(p1p2_ymax, p1p3_ymax, p2p3_ymax)    
    
    SET = []

    i = round(g_ymin)
    i = int(i)
    while(i <= g_ymax+1):
        SET.append([])
        i += 1

    i = round(p1p2_ymin)
    i = int(i)
    c = 0
    while(i <= round(p1p2_ymax)):
        SET[c].append([p1p2_xofymin, p1p2_dxdy, "p1p2", p1p2_ymin])
        i += 1
        c += 1

    i = round(p1p3_ymin)
    i = int(i)
    c = 0
    while(i <= round(p1p3_ymax)):
        SET[c].append([p1p3_xofymin, p1p3_dxdy, "p1p3", p1p3_ymin])
        i += 1
        c += 1

    i = round(p2p3_ymin)
    i = int(i)
    c = 0
    while(i <= round(p2p3_ymax)):
        SET[c].append([p2p3_xofymin, p2p3_dxdy, "p2p3", p2p3_ymin])
        i += 1
        c += 1

    y = round(g_ymin)
    y = int(y)
    c = 0
    res = []
    while(y <= round(g_ymax)):
        xlist = []
        idx = 0
        ye = SET[c]
        while(idx < len(ye)):
            e = ye[idx]
            if(y == e[3]):
                xlist.append(e[0])

            else:
                holder = 0
                if(e[2] == "p1p2"):
                    holder = p1p2.getHolder()
                elif(e[2] == "p1p3"):
                    holder = p1p3.getHolder()
                elif(e[2] == "p2p3"):
                    holder = p2p3.getHolder()

                e[0] = holder + e[1]
                
                if(e[2] == "p1p2"):
                    p1p2.updateHolder(e[0])
                elif(e[2] == "p1p3"):
                    p1p3.updateHolder(e[0])
                elif(e[2] == "p2p3"):
                    p2p3.updateHolder(e[0])

                e[0] = round(e[0])
                xlist.append(e[0])
            idx += 1
        xmin = min(xlist)
        xmax = max(xlist)
        res.append([y, xmin, xmax])
        y += 1
        c += 1
    
    
    pixels = []
    for el in res:
        pix1 = [el[1], el[0]]
        pix2 = [el[2], el[0]]
        IA = ([0, 0, 0])
        IB = ([0, 0, 0])
        if(pix1[0] == round(p1[0]) and pix1[1] == round(p1[1])):
            tmp = pixelI(pix1[0], pix1[1], I1)
            pixels.append(tmp)
            IA = I1
        elif(pix1[0] == round(p2[0]) and pix1[1] == round(p2[1])):
            tmp = pixelI(pix1[0], pix1[1], I2)
            pixels.append(tmp)
            IA = I2
        elif(pix1[0] == round(p3[0]) and pix1[1] == round(p3[1])):
            tmp = pixelI(pix1[0], pix1[1], I3)
            pixels.append(tmp)
            IA = I3
        
        if(pix2[0] == round(p1[0]) and pix2[1] == round(p1[1])):
            tmp = pixelI(pix2[0], pix2[1], I1)
            pixels.append(tmp)
            IB = I1
        elif(pix2[0] == round(p2[0]) and pix2[1] == round(p2[1])):
            tmp = pixelI(pix2[0], pix2[1], I2)
            pixels.append(tmp)
            IB = I2
        elif(pix2[0] == round(p3[0]) and pix2[1] == round(p3[1])):
            tmp = pixelI(pix2[0], pix2[1], I3)
            pixels.append(tmp)
            IB = I3
        
        else:
            # sisi A.1
            if(round(p1[1]) <= pix1[1] and pix1[1] <= round(p2[1])):
                # pix1 between p1 and p2
                t = 0
                if((p2[1]-p1[1]) == 0):
                    t = 0
                else:
                    t = ((pix1[1]-p1[1])/(p2[1]-p1[1]))
                I = np.add(I1, np.dot(t, np.subtract(I2, I1)))
                tmp = pixelI(pix1[0], pix1[1], I)
                pixels.append(tmp)
                IA = I
            elif(round(p1[1]) <= pix1[1] and pix1[1] <= round(p3[1])):
                # pix1 between p1 and p3
                t = ((pix1[1]-p1[1])/(p3[1]-p1[1]))
                I = np.add(I1, np.dot(t, np.subtract(I3, I1)))
                tmp = pixelI(pix1[0], pix1[1], I)
                pixels.append(tmp)
                IA = I
            elif(round(p2[1]) <= pix1[1] and pix1[1] <= round(p3[1])):
                # pix1 between p2 and p3
                t = 0
                if((p3[1]-p2[1]) == 0):
                    t = 0
                else:
                    t = ((pix1[1]-p2[1])/(p3[1]-p2[1]))
                I = np.add(I2, np.dot(t, np.subtract(I3, I2)))
                tmp = pixelI(pix1[0], pix1[1], I)
                pixels.append(tmp)
                IA = I
            # sisi A.2
            elif(round(p1[1]) >= pix1[1] and pix1[1] >= round(p2[1])):
                # pix1 between p1 and p20
                t = 0
                if((p1[1]-p2[1]) == 0):
                    t = 0
                else:
                    t = ((pix1[1]-p1[1])/(p2[1]-p1[1]))
                I = np.add(I1, np.dot(t, np.subtract(I2, I1)))
                tmp = pixelI(pix1[0], pix1[1], I)
                pixels.append(tmp)
                IA = I
            elif(round(p1[1]) >= pix1[1] and pix1[1] >= round(p3[1])):
                # pix1 between p1 and p3
                t = ((pix1[1]-p1[1])/(p3[1]-p1[1]))
                I = np.add(I1, np.dot(t, np.subtract(I3, I1)))
                tmp = pixelI(pix1[0], pix1[1], I)
                pixels.append(tmp)
                IA = I
            elif(round(p2[1]) >= pix1[1] and pix1[1] >= round(p3[1])):
                # pix1 between p2 and p3
                t = 0
                if((p2[1]-p3[1]) == 0):
                    t = 0
                else:
                    t = ((pix1[1]-p2[1])/(p3[1]-p2[1]))
                I = np.add(I2, np.dot(t, np.subtract(I3, I2)))
                tmp = pixelI(pix1[0], pix1[1], I)
                pixels.append(tmp)
                IA = I
            else:
                print("else1")
                print(pix1, p1, p2, p3)

            # sisi B.1
            if(round(p1[1]) <= pix2[1] and pix2[1] <= round(p2[1])):
                # pix2 between p1 and p2
                t = 0
                if((p2[1]-p1[1]) == 0):
                    t = 0
                else:
                    t = ((pix1[1]-p1[1])/(p2[1]-p1[1]))
                I = np.add(I1, np.dot(t, np.subtract(I2, I1)))
                tmp = pixelI(pix2[0], pix2[1], I)
                pixels.append(tmp)
                IB = I
            elif(round(p1[1]) <= pix2[1] and pix2[1] <= round(p3[1])):
                # pix2 between p1 and p3
                t = ((pix2[1]-p1[1])/(p3[1]-p1[1]))
                I = np.add(I1, np.dot(t, np.subtract(I3, I1)))
                tmp = pixelI(pix2[0], pix2[1], I)
                pixels.append(tmp)
                IB = I
            elif(round(p2[1]) <= pix2[1] and pix2[1] <= round(p3[1])):
                # pix2 between p2 and p3
                t = 0
                if((p3[1]-p2[1]) == 0):
                    t = 0
                else:
                    t = ((pix2[1]-p2[1])/(p3[1]-p2[1]))
                I = np.add(I2, np.dot(t, np.subtract(I3, I2)))
                tmp = pixelI(pix2[0], pix2[1], I)
                pixels.append(tmp)
                IB = I
            # sisi B.2
            elif(round(p1[1]) >= pix2[1] and pix2[1] >= round(p2[1])):
                # pix2 between p1 and p2
                t = 0
                if((p1[1]-p2[1]) == 0):
                    t = 0
                else:
                    t = ((pix2[1]-p1[1])/(p2[1]-p1[1]))
                I = np.add(I1, np.dot(t, np.subtract(I2, I1)))
                tmp = pixelI(pix2[0], pix2[1], I)
                pixels.append(tmp)
                IB = I
            elif(round(p1[1]) >= pix2[1] and pix2[1] >= round(p3[1])):
                # pix2 between p1 and p3
                t = ((pix2[1]-p1[1])/(p3[1]-p1[1]))
                I = np.add(I1, np.dot(t, np.subtract(I3, I1)))
                tmp = pixelI(pix2[0], pix2[1], I)
                pixels.append(tmp)
                IB = I
            elif(round(p2[1]) >= pix2[1] and pix2[1] >= round(p3[1])):
                # pix2 between p2 and p3
                t = 0
                if((p2[1]-p3[1]) == 0):
                    t = 0
                else:
                    t = ((pix2[1]-p2[1])/(p3[1]-p2[1]))
                I = np.add(I2, np.dot(t, np.subtract(I3, I2)))
                tmp = pixelI(pix2[0], pix2[1], I)
                pixels.append(tmp)
                IB = I
            else:
                print("else2")
                print(pix2, p1, p2, p3)

        
        x = el[1]+1
        xA = el[1]
        y = el[0]
        xB = el[2]
        dIx = ([0, 0, 0])
        if((xB-xA) == 0):
            dIx = ([0, 0, 0])
        elif((xB-xA) < 0):
            dIx = np.divide(np.subtract(IB, IA), abs(xB-xA))
        else:
            dIx = np.divide(np.subtract(IB, IA), (xB-xA))
        
        k = 0
        if((xB-xA) == 0):
            k = 0
        else:
            k = ((x-xA)/(xB-xA))
        IP = np.add(IA, np.dot(k, np.subtract(IB, IA)))

        while(x < xB):
            I = np.add(IP, dIx)
            tmp = pixelI(x, y, I)
            pixels.append(tmp)
            x += 1

    # for p in pixels:
    #     print(p.getAttributes())
    return pixels

class pixelI():
    def __init__(self, x, y, I):
        self.x = x
        self.y = y
        self.I = I

    def getAttributes(self):
        return [self.x, self.y, self.I]

    def getIntensity(self):
        return self.I

class edgeSET():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.ymin = self.findYmin(self.p1, self.p2)
        self.ymax = self.findYmax(self.p1, self.p2)
        self.xofymin = self.findXofymin(self.p1, self.p2)
        self.dx = self.findDx(self.p1, self.p2)
        self.dy = self.ymax - self.ymin
        self.holder = self.xofymin

    def findYmin(self, p1, p2):
        y1 = p1[1]
        y2 = p2[1]
        if(y1 > y2):
            return y2
        elif(y1 < y2):
            return y1
        else:
            return y1

    def findYmax(self, p1, p2):
        y1 = p1[1]
        y2 = p2[1]
        if(y1 > y2):
            return y1
        elif(y1 < y2):
            return y2
        else:
            return y1

    def findXofymin(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        if(y1 > y2):
            return x2
        elif(y1 < y2):
            return x1
        else:
            return min(x1, x2)

    def findDx(self, p1, p2):
        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]
        if(y1 > y2):
            return x1-x2
        elif(y1 < y2):
            return x2-x1
        else:
            return max(x1, x2) - min(x1, x2)

    def getAttributes(self):
        return [self.ymin, self.ymax, self.xofymin, self.dx, self.dy]

    def updateHolder(self, holder):
        self.holder = holder

    def getHolder(self):
        return self.holder


p1 = [7, 4, 4]
p2 = [3, 0, 5]
p3 = [1, 6, 2]
# res = findSET(p1, p2, p3)

# p1 = [0, 0, 0]
# p2 = [20, 0, 0]
# p3 = [20, 20, 0]
p1 = [0, 0, 0]
p2 = [20, 20, 0]
p3 = [0, 20, 0]
I1 = ([1, 1, 1])
I2 = ([1, 100, 1])
I3 = ([1, 50, 1])
# res2 = findGouraudSET(p1, p2, p3, I1, I2, I3)
# for r in res2:
#     print(r.getAttributes())