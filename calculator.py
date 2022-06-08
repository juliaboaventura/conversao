import method

while True:
    print('\nCalculadoras: \n[1] Decimal para outras bases \n[2] Outras bases para decimal \n[0] Sair')
    calc=int(input('Qual a opção de sua escolha? '))

    if calc==0: break

    elif calc==1:
        print('\nCalculadora decimal para outras bases')
        print('\n[1] Decimal para binário \n[2] Decimal para octal \n[3] Decimal para hexadecimal \n[4] Sobre o sistema \n[0] Sair')
        op = int(input('Digite uma opção: '))
        if op==1: 
                dec = int(input('Digite um número decimal: '))
                numE = dec
                print(method.dec2bin(dec, numE, bin))


        elif op==2:
            dec = int(input('Digite um número decimal: '))
            numE = dec
            oct = ''
            while dec != 0:
                r = dec%8
                oct = str(r) + oct
                dec = dec//8
            print(f'O octadecimal de {numE} é igual a {oct}')

        elif op==3:
            dec = int(input('Digite um número decimal: '))
            numE = dec
            conversion = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
            hex = ''
            while dec != 0:
                r = dec%16
                hex = conversion[r] + hex
                dec = dec//16
            print(f'O hexadecimal de {numE} é igual a {hex}')

        elif op==4:
            print('Grupo:')
        elif op==0: break
    
    elif calc==2:
        print('\nCalculadora para a base 10 (decimal)')
        print('\n[1] Binário para decimal \n[2] Octal para decimal \n[3] Hexadecimal para decimal \n[0] Sair')
        op = int(input('Digite uma opção: '))
        if op==1:
            bin = input('Digite um número binário: ')
            decimal = 0
            n= len(bin) -1
            for d in bin:
                decimal = decimal + int(d)*2**n
                n=n-1
            print(f'o número binário {bin} é igual a {decimal} na base 10')

        elif op==2:
            oct = input('Digite um número octadecimal: ')
            decimal = 0
            n= len(oct)-1
            for d in oct:
                decimal = decimal + int(d)*8**n
                n=n-1
            print(f'o número octadecimal {oct} é igual a {decimal} na base 10')

        elif op==3:
            hex = input('Digite um número hexadecimal: ')
            n = len(hex) 
            decimal = 0
            comt = 0
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
        elif op==0: break

    
