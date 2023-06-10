tokens = {
    "Coma": afd_coma,
    "PuntoYComa": afd_puntoycoma,
    "Entonces": afd_entonces,
    "Equal": afd_equal,
    "FinFunc": afd_finfunc,
    "FinSi": afd_finsi,
    "Func": afd_func,
    "FinSi": afd_finsi,
    "Hasta": afd_hasta,
    "Leer": afd_leer,
    "Mostrar": afd_mostrar,
    "Si": afd_si,
    "Sino": afd_sino,
    "Oprel": afd_oprel,
    "Opmult": afd_opmult,
    "Opsuma": afd_opsuma,
    "Id": afd_id,
    "Num": afd_num,
}


def afd_entonces(lexema):
  tabla = {
        'A': {'e': 'B'},
        'C': {'t': 'D'},
        'D': {'o': 'E'},
        'B': {'n': 'C'},
        'E': {'n': 'F'},
        'F': {'c': 'G'},
        'G': {'e': 'H'},
        'H': {'s': 'I'},
        'I': {},
        'T': {}
    }
  estado_actual='A'
  estados_finales=['I']
  for c in lexema:
    if c in tabla[estado_actual]:
      estado_actual = tabla[estado_actual][c]
    else:
      estado_actual = 'T'
      break
  if estado_actual in estados_finales:
      return "FINAL"
  elif estado_actual == 'T':
      return "TRAMPA"
  else:
      return "NO FINAL"
print(afd_entonces(input()))