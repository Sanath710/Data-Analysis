import numpy as np

def calculate(numbers):

    calc = {}
    if len(numbers) != 9 : raise ValueError("List should have exactly 9 numbers.")
    data = np.reshape(np.array(numbers),(3,3))
    
    calc['min'] = [np.min(data, axis=0).tolist(), np.min(data, axis=1).tolist(), np.min(data.flatten()).tolist()]
    calc['max'] = [np.max(data, axis=0).tolist(), np.max(data, axis=1).tolist(), np.max(data.flatten()).tolist()]
    calc['sum'] = [np.sum(data, axis=0).tolist(), np.sum(data, axis=1).tolist(), np.sum(data.flatten()).tolist()]
    calc['mean'] = [np.mean(data, axis=0).tolist(), np.mean(data, axis=1).tolist(), np.mean(data.flatten()).tolist()]
    calc['variance'] = [np.var(data, axis=0).tolist(), np.var(data, axis=1).tolist(), np.var(data.flatten()).tolist()]
    calc['standard deviation'] = [np.std(data, axis=0).tolist(), np.std(data, axis=1).tolist(), np.std(data.flatten()).tolist()]
    
    return calc