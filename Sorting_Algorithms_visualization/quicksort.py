import time
def partition(data, lo, hi, drawData, timeTick):
    s = lo
    pivot = data[hi]

    drawData(data, getColorArray(len(data), lo, hi, s, s))
    time.sleep(timeTick)

    for i in range(lo, hi):
        if data[i] < pivot:
            drawData(data, getColorArray(len(data), lo, hi, s, i, True))
            time.sleep(timeTick)

            data[s], data[i] = data[i], data[s]
            s += 1

        drawData(data, getColorArray(len(data), lo, hi, s, i))
        time.sleep(timeTick)

    drawData(data, getColorArray(len(data), lo, hi, s, hi, True))
    time.sleep(timeTick)

    data[s], data[hi] = data[hi], data[s]
    return s

def quick_sort(data, lo, hi, drawData, timeTick):
    if lo < hi:
        pi = partition(data, lo, hi, drawData, timeTick)
        quick_sort(data, lo, pi-1, drawData, timeTick)
        quick_sort(data, pi+1, hi, drawData, timeTick)


def getColorArray(dataLen, lo, hi, border, currIdx, isSwaping = False):
    colorArray = []
    for i in range(dataLen):
        if i >= lo and i <= hi:
            colorArray.append('#62B1F7')
        else:
            colorArray.append('white')

        if i == hi:
            colorArray[i] = '#AE6AF6'
        elif i == border:
            colorArray[i] = '#001AFA'
        elif i == currIdx:
            colorArray[i] = '#B04AFA'

        if isSwaping:
            if i == border or i == currIdx:
                colorArray[i] = '#7EA2E9'

    return colorArray