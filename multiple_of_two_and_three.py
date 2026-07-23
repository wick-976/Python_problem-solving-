n=int(input())

ser2={i*2 for i in range(1, n+1)}
ser3={i*3 for i in range(1, n+1)}

common=ser2 & ser3

print(sorted(ser2-common))

print(sorted((ser2 | ser3)- common))



   

   

    
    
    
    
