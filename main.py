print ('請輸入五個數字')
from myMath import myStatistics
S=[]
for t in range(5):
    i=int(input(''))
    S.append(i)
print(myStatistics.myMean(S))