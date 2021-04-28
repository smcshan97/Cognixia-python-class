def freq(str1):
    
    str1 = str1.split()         
    str2 = []
  
    for x in str1:             
  
        if x not in str2:
  
            str2.append(x)
              
    for x in range(0, len(str2)):
  
        print( str2[x], ' :', str1.count(str2[x]))   
  
def problem1():
    str1 = 'Hello HELLO worlD WORld hi'
    freq(str1.lower())                    
  
if __name__=="__main__":
    problem1()           
