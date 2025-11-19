import sys 

if len(sys.argv)==3:
    script_name=sys.argv[0]
    weight=sys.argv[1]
    height=sys.argv[2]

else:
    script_name=sys.argv[0]
    weight=50
    height=175
    print(f"No input so  deflaut values are taken as weight:{weight} height:{height}") 
        

weight=float(weight)
height=float(height)/100
BMI=weight/(height)*(height)
print("The weight is :",weight)
print("The height is :",height)
print("The BMI is :",BMI)
