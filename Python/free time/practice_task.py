Company_A=2000
Company_B=5000
time=0
while Company_A<Company_B:
    time+=1
    Company_B*=1.05
    Company_A*=1.15
    print(Company_A, Company_B)
print(time)