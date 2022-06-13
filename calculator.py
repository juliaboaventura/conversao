import method

while True:
    print('\nCalculadoras: \n[1] Decimal para outras bases \n[2] Outras bases para decimal \n[0] Sair')
    calc=int(input('Qual a opção de sua escolha? '))

    if calc==0: break

    elif calc==1:
        print('\nCalculadora decimal para outras bases')
        print('\n[1] Decimal para binário \n[2] Decimal para octal \n[3] Decimal para hexadecimal \n[0] Sair')
        op = int(input('Digite uma opção: '))
        if op==1: 
                dec = int(input('Digite um número decimal: '))
                numE = dec
                bin = ''
                method.dec2bin(dec, numE, bin)

        elif op==2:
            dec = int(input('Digite um número decimal: '))
            numE = dec
            oct = ''
            method.dec2oct(dec, numE, oct)

        elif op==3:
            dec = int(input('Digite um número decimal: '))
            numE = dec
            conversion = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
            hex = ''
            method.dec2hex(dec, numE, hex, conversion)

        elif op==0: break
    
    elif calc==2:
        print('\nCalculadora para a base 10 (decimal)')
        print('\n[1] Binário para decimal \n[2] Octal para decimal \n[3] Hexadecimal para decimal \n[0] Sair')
        op = int(input('Digite uma opção: '))
        if op==1:
            bin = input('Digite um número binário: ')
            decimal = 0
            n= len(bin) -1
            method.bin2dec(bin, decimal, n)

        elif op==2:
            oct = input('Digite um número octadecimal: ')
            decimal = 0
            n= len(oct)-1
            method.oct2dec(oct, decimal, n)

        elif op==3:
            hex = input('Digite um número hexadecimal: ')
            n = len(hex) 
            decimal = 0
            comt = 0
            method.hex2dec(hex, n, decimal, comt)
                
        elif op==0: break