import numpy as np

def calculate(digits):
    #exception error for not enough numbers in digits list
    if len(digits) < 9:
        raise ValueError("List must contain nine numbers.")
        
    
    np_array = np.zeros((3,3))
    
    #helper to track rows in np_array
    r = 0
    
    for x in range(0,9,3):
        new_row = [digits[x], digits[x+1], digits[x+2]]
        np_array[r] = new_row
      
        r += 1
    
    summary = {'mean': [], 
               'variance': [], 
               'standard deviation': [], 
               'max': [],
               'min': [],
               'sum': []
              }
    
   
    for x in range(2):
        summary['mean'].append(list(np.mean(np_array, axis=x)))
        summary['variance'].append(list(np.var(np_array, axis=x)))
        summary['standard deviation'].append(list(np.std(np_array, axis=x)))
        summary['max'].append(list(np.max(np_array, axis=x).astype(int)))
        summary['min'].append(list(np.min(np_array, axis=x).astype(int)))
        summary['sum'].append(list(np.sum(np_array, axis=x).astype(int)))
        
   
    for _ in range(1):
        summary['mean'].append(np.mean(np_array))
        summary['variance'].append(np.var(np_array))
        summary['standard deviation'].append(np.std(np_array))

        summary['max'].append(np.max(np_array).astype(int))
        summary['min'].append(np.min(np_array).astype(int))
        summary['sum'].append(np.sum(np_array).astype(int))
    
   
   
   



    return summary