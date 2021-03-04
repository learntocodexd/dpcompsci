def rotate(input,d):  
  
    # slice string in two parts for left and right  
    Lfirst = input[0 : d]  
    Lsecond = input[d :]  
    Rfirst = input[0 : len(input)-d]  
    Rsecond = input[len(input)-d : ]  
  
    # now concatenate two parts together  
    print("Left Rotation: ",(Lsecond + Lfirst)) 
    print("Right Rotation: ",(Rsecond + Rfirst))
    

text = "hello world"
number = 2

rotate(text, number)
