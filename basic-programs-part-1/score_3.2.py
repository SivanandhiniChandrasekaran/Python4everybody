score = input("Enter Score: ")
s = float(score)

if s>1.0:
    print("Error. Score out of range!")
elif s>0.0:
    if s>=0.90:
        print("A")

    elif s>=0.80:
        print("B")

    elif s>=0.70:
        print("C")

    elif s>=0.60:
        print("D")

    elif s<0.60:
        print("F")
else :
    print("Error. Score out of range!")
