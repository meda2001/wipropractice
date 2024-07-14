speed_limit=50
speed=65
if speed<=speed_limit:
    print("fine:  $0 " )
elif speed_limit<speed<= speed_limit+10:
    print("fine $50 ")
elif speed_limit+10<speed<= speed_limit+20:
    print("fine $100 ")
else:
    print("fine $1000")
