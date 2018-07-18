var numero = 1;
while (numero <= 20) {
	if (numero % 3 == 0) {
		console.log("Julia");
	}
	
	if (numero % 5 == 0) {
		console.log("James");
	}
			
	if (numero % 3 == 0 && numero % 5 == 0) {
		console.log("JuliaJames");
	}

	if (numero % 3 !=0 && numero % 5 != 0) {
		console.log(numero);
	}

	numero++;
}