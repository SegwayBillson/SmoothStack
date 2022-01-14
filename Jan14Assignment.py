def bmi_func(info):
    lines = info.split('\n')
    answer = ""

    for line in range(1,len(lines)):
        vals = lines[line].split()
        bmi = float(vals[0]) / (float(vals[1])**2)
        if(bmi < 18.5):
            answer += "under "
        elif(bmi < 25):
            answer += "normal "
        elif(bmi < 30):
            answer += "over "
        else:
            answer += "obese"

    return answer[:-1]

print(bmi_func("3\n80 1.73\n55 1.58\n49 1.91"))