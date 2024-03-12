import numpy as np

def calculate(lista):
    if len(lista) < 9:
        raise ValueError("List must contain nine numbers.")
    else:
        matrix = np.array(lista).reshape(3, 3)

        mean = [np.mean(matrix, axis=0).tolist(), np.mean(matrix, axis=1).tolist(), np.mean(matrix).tolist()]
        variance = [np.var(matrix, axis=0).tolist(), np.var(matrix, axis=1).tolist(), np.var(matrix).tolist()]
        std_dev = [np.std(matrix, axis=0).tolist(), np.std(matrix, axis=1).tolist(), np.std(matrix).tolist()]
        maximum = [np.max(matrix, axis=0).tolist(), np.max(matrix, axis=1).tolist(), np.max(matrix).tolist()]
        minimum = [np.min(matrix, axis=0).tolist(), np.min(matrix, axis=1).tolist(), np.min(matrix).tolist()]
        summation = [np.sum(matrix, axis=0).tolist(), np.sum(matrix, axis=1).tolist(), np.sum(matrix).tolist()]

        calculations = {
            'mean': mean,
            'variance': variance,
            'standard deviation': std_dev,
            'max': maximum,
            'min': minimum,
            'sum': summation
        }

    return calculations
