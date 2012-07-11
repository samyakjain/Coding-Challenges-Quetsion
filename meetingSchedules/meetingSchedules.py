import math,traceback
START_HOUR=0
START_MIN=1
END_HOUR=2
END_MIN=3
timeArray=[]

def splitMe(timeSlot):
    sh=int(timeSlot[START_HOUR])
    sm=int(timeSlot[START_MIN])
    eh=int(timeSlot[END_HOUR])
    em=int(timeSlot[END_MIN])
    timeSlots.remove(timeSlot)
    timeSlots.append([sh,sm,"23","59"])
    timeSlots.append(["00","00",eh,em])


for i in range(0,24):
    for j in range(0,60):
        timeArray.append((i*60)+j)

# mandatory= raw_input()
# mandatory=mandatory.split(" ")
# TotalBusyTimeSlots=int(mandatory[0])
# meetingToBeScheduledFor=int(mandatory[1])
TotalBusyTimeSlots=8
meetingToBeScheduledFor=60

i=0
timeSlots=[['08', '00', '10', '15'], ['22', '00', '23', '15'], ['17', '00', '19', '00'], ['07', '00', '09', '45'], ['09', '00', '13', '00'], ['16', '00', '17', '45'], ['12', '00', '13', '30'], ['11', '30', '12', '30']]
#busyDurationTimeArray=[]

def calculateTimeRange(timeSlot):
    sh=int(timeSlot[START_HOUR])
    sm=int(timeSlot[START_MIN])
    eh=int(timeSlot[END_HOUR])
    em=int(timeSlot[END_MIN])
    return sh*60+sm,eh*60+em
    
def decorateIt(elem):
    elem=str(elem)
    if elem=="24":
        return "00"
    if len(elem)==1:
        elem="0"+elem
    return elem

def convertTimeToArray(x,y):
    sh=str(int(x/60))
    sm=int(x%60)
    eh=int(y/60)
    em=int(y%60)
    if em == 59:
        em=0
        eh=eh+1
    else:
        em = em +1
#    sh=decorateIt(sh)
#    sm=decorateIt(sm)
#    eh=decorateIt(eh)
#    en=decorateIt(em)
    return [sh,sm,eh,em]
    
    
#print len(timeArray)
#while (i < TotalBusyTimeSlots):
#    timeSlots.append(raw_input().split(" "))
#    i=i+1
i=0
#print len(timeArray)
while(i < TotalBusyTimeSlots):
    if int(timeSlots[i][START_HOUR]) > int(timeSlots[i][END_HOUR]):
        splitMe(timeSlots[i])
        TotalBusyTimeSlots += 1
    #print timeSlots[i]
    x,y=calculateTimeRange(timeSlots[i])
    for j in range(x,y):
        if j in timeArray:
            timeArray.remove(j)
    #print len(timeArray)
    i=i+1

#x=timeArray[0]
realArray=[]
status=True
for i in range(0,len(timeArray) - 1 ):
    if status:
        x=timeArray[i]
        #print x
        status=False        
    try:
        b=timeArray[i+1]-timeArray[i]
    except:
        #traceback.print_exc()
        continue
    if b != 1:
        y=timeArray[i]
        realArray.append(convertTimeToArray(x,y))
        status=True
    elif timeArray[i+1] == timeArray[-1]:
        y=timeArray[i+1]
        realArray.append(convertTimeToArray(x,y))
        status=True

for res in realArray:
    x,y=calculateTimeRange(res)
    diff=math.fabs(x-y)
    if diff >= meetingToBeScheduledFor:
        print decorateIt(res[START_HOUR]) + " " + decorateIt(res[START_MIN]) + " " + decorateIt(res[END_HOUR]) + " " + decorateIt(res[END_MIN])