def dec2bin(dec, numE, bin):
    bin = ''
    while dec != 0:
        r = dec%2
        bin = str(r) + bin
        dec = dec//2   
    return(print(f'O binário de {numE} é igual a {bin}'))
    