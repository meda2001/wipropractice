temperature=[]
for day in range(1,8):
    temp=int(input(f"enter the temperature for the day{day}:"))
    temperature.append(temp)
average_temp=sum(temperature)/len(temperature)
print(average_temp)

highest_temp=print(max(temperature))
lowest_temp=print(min(temperature))
