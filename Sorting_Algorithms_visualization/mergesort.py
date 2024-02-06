import time
def merge_sort(data, drawData, timeTick):
    merge_sort_alg(data,0, len(data)-1, drawData, timeTick)

def merge_sort_alg(data, lo, hi, drawData, timeTick):
    if hi <= lo:
        return

    mid = (lo + hi) // 2
    merge_sort_alg(data, lo, mid, drawData, timeTick)
    merge_sort_alg(data, mid+1, hi, drawData, timeTick)
    merge(data, lo, mid, hi, drawData, timeTick)

def merge(data, lo, mid, hi, drawData, timeTick):
    drawData(data, getColorArray(len(data), lo, mid, hi))
    time.sleep(timeTick)

    leftPart = data[lo:mid+1]
    rightPart = data[mid+1: hi+1]

    leftIdx = rightIdx = 0

    for dataIdx in range(lo, hi+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1
        
        elif leftIdx < len(leftPart):
            data[dataIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            data[dataIdx] = rightPart[rightIdx]
            rightIdx += 1
    
    drawData(data, ["#7EA2E9" if x >= lo and x <= hi else "#001AFA" for x in range(len(data))])
    time.sleep(timeTick)

def getColorArray(leght, lo, mid, hi):
    colorArray = []

    for i in range(leght):
        if i >= lo and i <= hi:
            if i >= lo and i <= mid:
                colorArray.append("#62B1F7")
            else:
                colorArray.append("#AE6AF6")
        else:
            colorArray.append("#B04AFA")  

    return colorArray
