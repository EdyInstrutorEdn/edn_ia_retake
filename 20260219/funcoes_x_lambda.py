def func_somar(a, b):
    return a + b

lambda_somar = lambda a, b: a + b

soma1 = func_somar(5, 3)
soma2 = lambda_somar(5, 3) 
print(f"Soma usando função tradicional: {soma1}")
print(f"Soma usando função lambda: {soma2}")    
