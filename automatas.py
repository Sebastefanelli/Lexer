VT = ["DerParen", "IzqParen", "PuntoYComa", "Entonces", "Equal", "FinFunc", "FinSi", "Func",
      "Hasta", "Leer", "Mostrar", "Repetir", "Si", "Sino", "Oprel", "Opmult",
      "Opsuma", "Num", "Id", "#"]

VN = ["Program", "ListaSentencias", "ListaSentencias_p", "Sentencia", "SentenciaSi", "SentenciaSi_p", "SentenciaRepetir", "SentenciaAsig", "SentenciaLeer",
      "SentenciaMostrar", "SentenciaFun", "Proc", "ListaPar", "ListaPar_p", "Expresion", "Expresion_p", "Expresion2", "Expresion2_p", "Termino", "Termino_p", "Factor", ]

simbolo_inicial = "Program"

P = {
    "Program": [
        ["ListaSentencias"]
    ],

    "ListaSentencias": [
        ["Sentencia", "ListaSentencias_p"],
    ],

    "ListaSentencias_p": [
        ["PuntoYComa", "Sentencia", "ListaSentencias_p"],
        [],
    ],

    "Sentencia": [
        ["SentenciaSi"],
        ["SentenciaRepetir"],
        ["SentenciaAsig"],
        ["SentenciaLeer"],
        ["SentenciaMostrar"],
        ["SentenciaFun"],
    ],

    "SentenciaRepetir": [
        ["Repetir", "ListaSentencias", "Hasta", "Expresion"]
    ],

    "SentenciaSi": [
        ["Si", "Expresion", "Entonces", "ListaSentencias", "SentenciaSi_p"]
    ],

    "SentenciaSi_p": [
        ["Sino", "ListaSentencias", "FinSi"],
        ["FinSi"]
    ],

    "SentenciaAsig": [
        ["Id", "Equal", "Expresion"]
    ],

    "SentenciaLeer": [
        ["Leer", "Id"]
    ],

    "SentenciaMostrar": [
        ["Mostrar", "Expresion"]
    ],

    "SentenciaFun": [
        ["Func", "Proc", "FinFunc"]
    ],

    "Proc": [
        ["Id", "IzqParen", "ListaPar", "DerParen", "ListaSentencias"]
    ],

    "ListaPar": [
        ["Id", "ListaPar_p"],
    ],

    "ListaPar_p": [
        ["PuntoYComa", "Id", "ListaPar_p"],
        []
    ],

    "Expresion": [
        ["Expresion2", "Expresion_p"],
    ],

    "Expresion_p": [
        ["oprel", "Expresion2"],
        [],
    ],

    "Expresion2": [
        ["Termino", "Expresion2_p"]
    ],

    "Expresion2_p": [
        ["Opsuma", "Termino", "Expresion2_p"],
        []
    ],

    "Termino": [
        ["Factor", "Termino_p"]
    ],

    "Termino_p": [
        ["Opmult", "Factor", "Termino_p"],
        []
    ],

    "Factor": [
        ["IzqParen", "Expresion", "DerParen"],
        ["Num"],
        ["Id"]
    ]
}

SD = {
    "Program": {
        "Si": ["ListaSentencias"],
        "Repetir": ["ListaSentencias"],
        "Id": ["ListaSentencias"],
        "Leer": ["ListaSentencias"],
        "Mostrar": ["ListaSentencias"],
        "Func": ["ListaSentencias"],

    },

    "ListaSentencias": {
        "Si": ["Sentencia", "ListaSentencias_p"],
        "Repetir": ["Sentencia", "ListaSentencias_p"],
        "Id": ["Sentencia", "ListaSentencias_p"],
        "Leer": ["Sentencia", "ListaSentencias_p"],
        "Mostrar": ["Sentencia", "ListaSentencias_p"],
        "Func": ["Sentencia", "ListaSentencias_p"],
    },

    "ListaSentencias_p": {
        "PuntoYComa": ["PuntoYComa", "Sentencia", "ListaSentencias_p"],
        "#": [],
        "FinFunc": [],
        "FinSi": [],
        "Sino": [],
        "Hasta": [],
    },

    "Sentencia": {
        "Si": ["SentenciaSi"],
        "Repetir": ["SentenciaRepetir"],
        "Id": ["SentenciaAsig"],
        "Leer": ["SentenciaLeer"],
        "Mostrar": ["SentenciaMostrar"],
        "Func": ["SentenciaFun"],
    },

    "SentenciaRepetir": {
        "Repetir":  ["Repetir", "ListaSentencias", "Hasta", "Expresion"],
    },

    "SentenciaSi": {
        "Si":  ["Si", "Expresion", "Entonces", "ListaSentencias",
                "SentenciaSi_p"],
    },

    "SentenciaSi_p": {
        "Sino": ["Sino", "ListaSentencias", "FinSi"],
        "FinSi": ["FinSi"],
    },

    "SentenciaAsig": {
        "Id": ["Id", "Equal", "Expresion"],
    },

    "SentenciaLeer": {
        "Leer": ["Leer", "Id"],
    },

    "SentenciaMostrar": {
        "Mostrar": ["Mostrar", "Expresion"],
    },

    "SentenciaFun": {
        "Func": ["Func", "Proc", "FinFunc"],
    },

    "Proc": {
        "Id": ["Id", "IzqParen", "ListaPar", "DerParen", "ListaSentencias"],
    },

    "ListaPar": {
        "Id": ["Id", "ListaPar_p"],
    },

    "ListaPar_p": {
        "PuntoYComa": ["PuntoYComa", "Id", "ListaPar_p"],
        "DerParen": [],
    },

    "Expresion": {
        "IzqParen": ["Expresion2", "Expresion_p"],
        "Num": ["Expresion2", "Expresion_p"],
        "Id": ["Expresion2", "Expresion_p"],
    },

    "Expresion_p": {
        "Oprel": ["Oprel", "Expresion2"],
        "DerParen": [],
        "#": [],
        "PuntoYComa": [],
        "FinFunc": [],
        "FinSi": [],
        "Sino": [],
        "Hasta": [],
        "Entonces": [],
    },

    "Expresion2": {
        "IzqParen": ["Termino", "Expresion2_p"],
        "Num": ["Termino", "Expresion2_p"],
        "Id": ["Termino", "Expresion2_p"],
    },

    "Expresion2_p": {
        "Opsuma": ["Opsuma", "Termino", "Expresion2_p"],
        "Oprel": [],
        "DerParen": [],
        "#": [],
        "PuntoYComa": [],
        "FinFunc": [],
        "FinSi": [],
        "Sino": [],
        "Hasta": [],
        "Entonces": [],
    },

    "Termino": {
        "IzqParen": ["Factor", "Termino_p"],
        "Num": ["Factor", "Termino_p"],
        "Id": ["Factor", "Termino_p"],
    },

    "Termino_p": {
        "Opmult": ["Opmult", "Factor", "Termino_p"],
        "Opsuma": [],
        "Oprel": [],
        "DerParen": [],
        "#": [],
        "PuntoYComa": [],
        "FinFunc": [],
        "FinSi": [],
        "Sino": [],
        "Hasta": [],
        "Entonces": [],
    },

    "Factor": {
        "IzqParen": ["IzqParen", "Expresion", "DerParen"],
        "Num": ["Num"],
        "Id": ["Id"]
    }
}
def afd_der_paren(lexema):
    if lexema == ")":
        return "FINAL"
    else:
        return "TRAMPA"


def afd_izq_paren(lexema):
    if lexema == "(":
        return "FINAL"
    else:
        return "TRAMPA"


def afd_id(lexema):
    estados = ['A', 'B', 'T']
    estados_finales = ['B']
    estado_actual = 'A'
    for c in lexema:
        if estado_actual == 'A' and c.isalpha():
            estado_actual = 'B'
        elif estado_actual == 'B' and c.isalnum():
            estado_actual = 'B'
        else:
            estado_actual = 'T'
            break

    if estado_actual in estados_finales:
        return "FINAL"
    else:
        return "TRAMPA"


def afd_num(lexema):
    if lexema.isnumeric():
        return "FINAL"
    else:
        return "TRAMPA"


def afd_puntoycoma(lexema):
    if lexema == ";":
        return "FINAL"
    else:
        return "TRAMPA"

def automata_por_tabla(lexema, tabla, estados_finales, estado_inicial):
    estado_actual = estado_inicial
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


def afd_entonces(lexema):
    tabla = {
        'A': {'e': 'B'},
        'B': {'n': 'C'},
        'C': {'t': 'D'},
        'D': {'o': 'E'},
        'E': {'n': 'F'},
        'F': {'c': 'G'},
        'G': {'e': 'H'},
        'H': {'s': 'I'},
        'I': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["I"], "A")


def afd_equal(lexema):
    tabla = {
        'A': {'e': 'B'},
        'B': {'q': 'C'},
        'C': {'u': 'D'},
        'D': {'a': 'E'},
        'E': {'l': 'F'},
        'F': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["F"], "A")


def afd_finfunc(lexema):
    tabla = {
        'A': {'f': 'B'},
        'B': {'i': 'C'},
        'C': {'n': 'D'},
        'D': {'f': 'E'},
        'E': {'u': 'F'},
        'F': {'n': 'G'},
        'G': {'c': 'H'},
        'H': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["H"], "A")


def afd_finsi(lexema):
    tabla = {
        'A': {'f': 'B'},
        'B': {'i': 'C'},
        'C': {'n': 'D'},
        'D': {'s': 'E'},
        'E': {'i': 'F'},
        'F': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["F"], "A")


def afd_func(lexema):
    tabla = {
        'A': {'f': 'B'},
        'B': {'u': 'C'},
        'C': {'n': 'D'},
        'D': {'c': 'E'},
        'E': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["E"], "A")


def afd_hasta(lexema):
    tabla = {
        'A': {'h': 'B'},
        'B': {'a': 'C'},
        'C': {'s': 'D'},
        'D': {'t': 'E'},
        'E': {'a': 'F'},
        'F': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["F"], "A")


def afd_leer(lexema):
    tabla = {
        'A': {'l': 'B'},
        'B': {'e': 'C'},
        'C': {'e': 'D'},
        'D': {'r': 'E'},
        'E': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["E"], "A")


def afd_mostrar(lexema):
    tabla = {
        'A': {'m': 'B'},
        'B': {'o': 'C'},
        'C': {'s': 'D'},
        'D': {'t': 'E'},
        'E': {'r': 'F'},
        'F': {'a': 'G'},
        'G': {'r': 'H'},
        'H': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["H"], "A")


def afd_repetir(lexema):
    tabla = {
        'A': {'r': 'B'},
        'B': {'e': 'C'},
        'C': {'p': 'D'},
        'D': {'e': 'E'},
        'E': {'t': 'F'},
        'F': {'i': 'G'},
        'G': {'r': 'H'},
        'H': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["H"], "A")


def afd_opmult(lexema):
    tabla = {
        'A': {"*": "B", "/": "B"},
        'B': {},
        'T': {},
    }
    return automata_por_tabla(lexema, tabla, ["B"], "A")


def afd_oprel(lexema):
    tabla = {
        'A': {">": "B", "<": "C", "=": "D"},
        'B': {"=": "D"},
        'C': {">": "D", "=": "D"},
        'D': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["B", "C", "D"], "A")


def afd_opsuma(lexema):
    tabla = {
        'A': {"+": "B", "-": "B"},
        'B': {},
        'T': {},
    }
    return automata_por_tabla(lexema, tabla, ["B"], "A")


def afd_si(lexema):
    tabla = {
        'A': {'s': 'B'},
        'B': {'i': 'C'},
        'C': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["C"], "A")


def afd_sino(lexema):
    tabla = {
        'A': {'s': 'B'},
        'B': {'i': 'C'},
        'C': {'n': 'D'},
        'D': {'o': 'E'},
        'E': {},
        'T': {}
    }
    return automata_por_tabla(lexema, tabla, ["E"], "A")



tokens = {
    "DerParen": afd_der_paren,
    "IzqParen": afd_izq_paren,
    "PuntoYComa": afd_puntoycoma,
    "Entonces": afd_entonces,
    "Equal": afd_equal,
    "FinFunc": afd_finfunc,
    "FinSi": afd_finsi,
    "Func": afd_func,
    "Hasta": afd_hasta,
    "Leer": afd_leer,
    "Mostrar": afd_mostrar,
    "Repetir": afd_repetir,
    "Si": afd_si,
    "Sino": afd_sino,
    "Oprel": afd_oprel,
    "Opmult": afd_opmult,
    "Opsuma": afd_opsuma,
    "Num": afd_num,
    "Id": afd_id,
}


def lexer(programa):
    programa = programa.strip()
    programa += " "

    tokens_out = [] 
    tokens_posibles = [t for t in tokens] 
    tokens_posibles_1mas = tokens_posibles.copy()
    lexema = ""
    lexema1mas = ""
    for i in range(len(programa)):
        lexema = lexema1mas
        lexema1mas = lexema1mas + programa[i]
        if tokens_posibles == []:
            for token in tokens:
                if tokens[token](lexema) != "TRAMPA":
                    tokens_posibles.append(token)
            tokens_posibles_1mas = tokens_posibles.copy()
        else:
            tokens_posibles = tokens_posibles_1mas.copy()
        if lexema == " " or lexema == "\n" or lexema == "\t":
            lexema1mas = programa[i]
            continue
        tokens_final = []
        for token in tokens_posibles:
            estado_1mas = tokens[token](lexema1mas)
            if estado_1mas == "TRAMPA":
                tokens_posibles_1mas.remove(token)
            estado_actual = tokens[token](lexema)
            if estado_actual == "FINAL":
                tokens_final.append(token)
        if tokens_posibles_1mas == []:
            if tokens_final != []:
                tokens_out.append({tokens_final[0]: lexema})
                lexema1mas = programa[i]
                tokens_posibles = []
            else:
                raise ValueError("Token invalido")

    return tokens_out


def parser(lista):
    lista.append(("#", "#"))
    datos_locales = {
        'tokens': lista,
        'index': 0,
        'error': False,
        'error_t': None,
    }

    def procesar(cadena):
        for simbolo in cadena:
            actual = datos_locales['tokens'][datos_locales['index']][0]
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == actual:
                    datos_locales['index'] += 1
                else:
                    datos_locales['error'] = True
            elif simbolo in VN:
                procedimiento_PNI(simbolo)
                if datos_locales['error']:
                    break

    def procedimiento_PNI(simbolo):
        datos_locales['error'] = False
        actual = datos_locales['tokens'][datos_locales['index']][0]
        simbolos_directrices = SD[simbolo]
        if actual in simbolos_directrices:
            procesar(simbolos_directrices[actual])
        else:
            datos_locales['error'] = True

    def principal():
        procedimiento_PNI(simbolo_inicial)
        actual = datos_locales['tokens'][datos_locales['index']][0]
        if actual != '#' or datos_locales['error']:
            print('la cadena no pertenece al lenguaje ')
            return False
        print('la cadena pertence al lenguaje')

        return True

    return principal()


tests = [
    # test 1
    '''
x equal 98234;

si 6 < 7 entonces
    x equal x / 4
sino
    x equal x / 3
finsi
''',

    # test 2
    '''
func mult(n1; n2)
    x equal n1 * n2;
    mostrar x
finfunc
''',

    # test 3
    '''
leer x;

i equal 0;
repetir
    mostrar i;
    i equal i + 1
hasta i = x
''',

    # test 4
    '''
23hola+-sifinsi
''',

    # test 5
    ''' 
repetir
    iequali+1;
    leerx;
    x=x*x;
    mostrarx
hasta i=33
''',

    # test 6
    ''' 
vmax=0;
leer y;
si y>vmax entonces
    vmax equal y
sino
    e equal e+1
finsi
mostrar vmax;
mostrar e
''',

    # test 7
    '''
repetir
    i equal i+1;
    leer nombre;
    leer edad;
    si edad>=18 entonces 
        mostrar nombre
    sino
        vdif equal 18-edad;
        mostrar vdif
    finsi
hasta i=20
''',

    # test 8
    '''
leer x;
leer y;
si x>y entonces 
    x equal x+y
sino
    y equal x+y
finsi
''',

    # test 9
    '''
func rest(n1; n2)
    x equal n1 - n2;
    mostrar x
finfunc
''',

    # test 10
    '''
vmax equal 0;
repetir
    i equal i+1;
    leer socio;
    leer dni;
    leer edad;
    si edad>vmax entonces 
        msocio equal socio;
        mdni equal dni;
        medad equal edad
    finsi
hasta i=50;
mostrar msocio;
mostrar mdni;
mostrar medad
''',
]


for i in range(len(tests)):
    print(f'=========TEST N°{i+1}=========')
    print(tests[i])
    print(f'---- RESULTADO \t {parser(lexer(tests[i]))}')
    print("")
    print("")

