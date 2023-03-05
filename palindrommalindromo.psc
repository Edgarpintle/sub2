Algoritmo palindrommalindromo
	Definir a,b,x como entero
	Definir num Como Caracter
	Escribir " Escribe un numero "
	Leer num
	b = Longitud ( num )
	a = 1 
	x = 0
	Mientras a < b Hacer
		si Subcadena( num , a , a )<> Subcadena( num , b , b ) Entonces
			x = x + 1	
		FinSi
		
			
		a = a  + 1
		b = b  -  1
		
	FinMientras
	si x == 0 Entonces
		Escribir  " El numero  " , num , " es palindromo "
	SiNo
		Escribir  " El numero " , num , " es polindromo "
		
	FinSi
FinAlgoritmo


