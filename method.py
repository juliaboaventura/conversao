def dec2bin(dec, numE, bin):
    while dec != 0:
        r = dec%2
        bin = str(r) + bin
        dec = dec//2   
    return(print(f'O binário de {numE} é igual a {bin}'))

def dec2oct(dec, numE, oct):
    while dec != 0:
        r = dec%8
        oct = str(r) + oct
        dec = dec//8
    return(print(f'O octadecimal de {numE} é igual a {oct}'))

def dec2hex(dec, numE, hex, conversion):
    while dec != 0:
        r = dec%16
        hex = conversion[r] + hex
        dec = dec//16
    return(print(f'O hexadecimal de {numE} é igual a {hex}'))

def bin2dec(bin, decimal, n):
    for d in bin:
        decimal = decimal + int(d)*2**n
        n=n-1
    print(f'O número binário {bin} é igual a {decimal} na base 10')

def oct2dec(oct, decimal, n):
    for d in oct:
        decimal = decimal + int(d)*8**n
        n=n-1
    print(f'o número octadecimal {oct} é igual a {decimal} na base 10')

def hex2dec(hex, n, decimal, comt):
    for d in hex:
        if d in 'Ff':
            comt = 15
            decimal = decimal + comt * 16 ** (n-1)
            n = n - 1
        elif d in 'Ee':
            comt = 14
            decimal = decimal + comt * 16 ** (n-1)
            n = n - 1
        elif d in 'Dd':
            comt = 13
            decimal = decimal + comt * 16 ** (n-1)
            n = n - 1
        elif d in 'Cc':
            comt = 12
            decimal = decimal + comt * 16 ** (n-1)
            n = n - 1
        elif d in 'Bb':
            comt = 11
            decimal = decimal + comt * 16 ** (n-1)
            n = n - 1
        elif d in 'Aa':
            comt = 10
            decimal = decimal + comt * 16 ** (n-1)
            n = n - 1
        else:        
            decimal = decimal + int(d) * 16 ** (n-1)
            n = n - 1
    print(f'O número hexadecimal {hex} é igual a {decimal} na base 10')

