import random

students = ["MA","TB","CB","MB","KC","HC","AC","JD","BF","BG","CH","BK","GL","DM","RN","NP","FS","KS","AW","BZ"]
pool = students*3

for student in students:
    critiques = set()
    for i in range(0, 3):
        critique = random.choice(pool)
        while(critique == student or critique in critiques):
            critique = random.choice(pool)
        critiques.add(critique)
        pool.remove(critique)
    print(student + ': ' + "{}".format(critiques))
