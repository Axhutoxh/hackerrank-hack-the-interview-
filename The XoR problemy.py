#code done by Ashutosh Chandra





def maxXorValue(x, k):
    new_string=''
    l1=list(x)		#converting a string into list 
			#string a=['1234'] convert into list l1=['1','2','3',4']

            
    for _ in range(len(l1)):	#loop runs from 0 to n 
        a=int(l1[_])		#in each iteration list object convert to int and assign to a variable


	 if k>a and a == 0:	#if condition satisfy add 1 in string new and decrement the value of k by -1
            new = new + str(1)
            k = k-1
        elif k>a and a == 1 :	#if condition satisfy add 0 in string new 
            
            new = new + str(0)
        else:
            new = new + str(0)	#if both conditon doesn't satisfy add 0 to the string
    print(new)





if __name__ == '__main__':
    
    t = int(input())

    for t_itr in range(t):
        s = input()

        k = int(input())

        y = maxXorValue(s, k)

