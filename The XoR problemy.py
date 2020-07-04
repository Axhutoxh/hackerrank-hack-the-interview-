#code done by Ashutosh Chandra





def maxXorValue(x, k):
    new_string=''
    l1=list(x)		#converting a string into list 
			#string a=['1234'] convert into list l1=['1','2','3',4']

            
    for _ in range(len(l1)):	#loop runs from 0 to n 
        a=int(l1[_])		#in each iteration list object convert to int and assign to a variable
        if k>a and a == 0:
            new = new + str(1)
            k = k-1
        elif k>a and a == 1 :
            
            new = new + str(0)
        else:
            new = new + str(0)
    print(new)





if __name__ == '__main__':
    
    t = int(input())

    for t_itr in range(t):
        s = input()

        k = int(input())

        y = maxXorValue(s, k)

