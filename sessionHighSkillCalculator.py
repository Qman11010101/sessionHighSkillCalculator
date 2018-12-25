import random
from tqdm import tqdm

print("Session Highスキルボーナス量確率計算機")
print("")

sesHigh = [200] * 99 + [-10000]
amountNotes = input("J-Criticalの量を入力してください>> ")
loopTimes = input("試行回数を入力してください>> ")
realLpTime = 0
expectedBonus = []

for times in tqdm(range(0, int(loopTimes))):
    vScore = 0

    for calc in range(0, int(amountNotes)):
        resRd = random.choice(sesHigh)
        vScore = vScore + int(resRd)
    
    realLpTime += 1
    expectedBonus.append(int(vScore))

print("")
print("全試行の平均値は" + str(round(sum(expectedBonus) / len(expectedBonus))))
print("")
print("最大値は" + str(max(expectedBonus)))
print("最小値は" + str(min(expectedBonus)))
input("Enterを押して終了")