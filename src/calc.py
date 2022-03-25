def get_fractions(entrada)
 numero = 0
  try:
    if(isinstance(entrada,str)):
      print(entrada)
      if "/" in entrada :
        arr = entrada.split("/")
        numerador = arr[0]
        denominador = arr[1]
        #print(arr)
        numero = float(numerador) / float(denominador)
        #print(arr, numero)
      else:
        numero = float(entrada)
        print(type(numero))
      
    if(isinstance(entrada,int) or  isinstance(entrada,float)):
      numero = entrada
  except:
    print("Error de formato de numero")
    
  return numero
