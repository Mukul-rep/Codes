import time
import array

start = time.process_time()
def arrayr():
#With Array Renaming
    a = array.array('q')
    for i in range(1000): 
        a.append(i)
    
    a1 = array.array('q') 
    for i in range(1000): 
        a1.append(i)
    y = array.array('q') 
    for i in range(1000): 
        y.append(i)

    b = array.array('q') 
    for i in range(1000): 
        b.append(i)
    for i in range(0,999):       
        a1[i] = a[i-1] + 3
        y[i] = a1[i] + 5
        a[i] = b[i]     
    end = time.process_time()
    print("With Array Renaming",end - start)
    
if __name__ == "__main__":
    t = threading.Thread(target=arrayr)
    t.start()
    t.join()   
    print("Done!") 
    
    
