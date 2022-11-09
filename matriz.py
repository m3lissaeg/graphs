def paseo_euleriano(matriz):
  euleriano = True
  node_position = 0
  for idx_fila, fila in enumerate(matriz):
    sum_fila = sum(fila)
    if (sum_fila%2 != 0):
      euleriano = False
      node_position = idx_fila
      break
        
  return {"available_path": euleriano} if euleriano else {"available_path": euleriano,"node_position": node_position}
  # return {"available_path": euleriano,"node_position": node_position}


# True - muestra el camino
# False - si tiene vertices de grado impar

if __name__ == '__main__':
  matriz = [
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
          ]
  print(paseo_euleriano(matriz))

