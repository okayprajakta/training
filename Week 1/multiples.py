def multiples(num):
    d={
            "statuscode": -1,
            "statusmessage": "Failed to get multiples because input is zero",
            "data": None
        }
    if num==0:
        return d
    else:
        d["statuscode"]=1
        d["statusmessage"]="Failed to get multiples because input is zero"
    num
    multiples = [num * i for i in range(1, 6)]
    return {
        "statuscode": 1,
        "statusmessage": "Got successful",
        "data": multiples
    }
 
print(multiples(int(input("Enter Num: "))))
