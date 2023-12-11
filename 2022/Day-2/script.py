dic = {
"A X":4,
"A Y":8,
"A Z":3,
"B X":1,
"B Y":5,
"B Z":9,
"C X":7,
"C Y":2,
"C Z":6
}
dic2 = {
"A X":"A Z",
"A Y":"A X",
"A Z":"A Y",
"B X":"B X",
"B Y":"B Y",
"B Z":"B Z",
"C X":"C Y",
"C Y":"C Z",
"C Z":"C X"
}
with open("input.txt", "r") as inp:
    ans = 0
    lines = inp.readlines()

    for line in lines:
        ans += dic[dic2[line.strip()]]
    
    print(ans)