document.getElementById('form').addEventListener('submit', function(event) {
    var fechaInput = document.getElementById('fecha');
    if (fechaInput.value === '') {
        setErrorFor(rut, 'No puede dejar Fecha en blanco');
	} else {
		setSuccessFor(rut);
    }
});

const form = document.getElementById('form');
const rut = document.getElementById('rut');
const nombre = document.getElementById('name');
const paterno = document.getElementById('paterno');
const materno = document.getElementById('materno');
const fecha = document.getElementById('fecha');
const telefono = document.getElementById('telefono');
const email = document.getElementById('email');
const direccion = document.getElementById('direccion');

form.addEventListener('submit', e => {
	e.preventDefault();
	
	checkInputs();
});



function checkInputs() {
	// trim to remove the whitespaces}

	const rutValue = rut.value.trim();
    const nombreValue = nombre.value.trim();
    const paternoValue = paterno.value.trim();
	const maternoValue = materno.value.trim();
	const fechaValue = fecha.value.trim();
	const telefonoValue = telefono.value.trim();
	const emailValue = email.value.trim();
	const direccionValue = direccion.value.trim();

	
	if(rutValue === '') {
		setErrorFor(rut, 'No puede dejar el Rut en blanco');
	} else {
		setSuccessFor(rut);
	}

    if(nombreValue === '') {
		setErrorFor(nombre, 'No puede dejar el Nombre en blanco');
	} else {
		setSuccessFor(nombre);
	}

    if(paternoValue === '') {
		setErrorFor(paterno, 'No puede dejar el Apellido Paterno en blanco');
	} else {
		setSuccessFor(paterno);
	}

	if(maternoValue === '') {
		setErrorFor(materno, 'No puede dejar el Apellido Materno en blanco');
	} else {
		setSuccessFor(materno);
	}

	if(fechaValue === '') {
		setErrorFor(fecha, 'No puede dejar fecha en blanco');
	} else {
		setSuccessFor(fecha);
	}
		
	if(telefonoValue === '') {
		setErrorFor(telefono, 'Telefono no debe ingresar en blanco.');
	} else {
		setSuccessFor(telefono);
	}
	if(emailValue === '') {
		setErrorFor(email, 'No puede dejar el email en blanco');
	} 	else if (!isEmail(emailValue)) {
		setErrorFor(email, 'Email invalido');
	} else {
		setSuccessFor(email);
	}
	
	if(direccionValue === '') {
		setErrorFor(direccion, 'Direccion no debe ingresar en blanco');
	} else{
		setSuccessFor(direccion);
	}
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}

function isEmail(email) {
	return /^(([^<>()\[\]\\.,;:\s@”]+(\.[^<>()\[\]\\.,;:\s@”]+)*)|(“.+”))@((\[[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}\.[0–9]{1,3}])|(([a-zA-Z\-0–9]+\.)+[a-zA-Z]{2,}))$/.test(email);
}