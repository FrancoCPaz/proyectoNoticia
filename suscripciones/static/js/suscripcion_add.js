const form = document.getElementById('form');
const rut = document.getElementById('rut');
const nombre = document.getElementById('name');
const apellidopa = document.getElementById('paterno');
const apellidoma = document.getElementById('materno');
const fecha = document.getElementById('fecha');
const telefono = document.getElementById('telefono');
const email = document.getElementById('email');
const direccion = document.getElementById('direccion');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');

form.addEventListener('submit', e => {
	e.preventDefault();
	
	checkInputs();
});

function checkInputs() {
	// trim to remove the whitespaces}
	const rutValue = rut.value.trim();
    const nombreValue = nombre.value.trim();
    const apellidopaValue = apellidopa.value.trim();
	const apellidomaValue = apellidoma.value.trim();
	const fechaValue = fecha.value.trim();
	const telefonoValue = telefono.value.trim();
	const emailValue = email.value.trim();
	const direccionValue = direccion.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();
	
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

    if(apellidopaValue === '') {
		setErrorFor(apellidopa, 'No puede dejar el Apellido Paterno en blanco');
	} else {
		setSuccessFor(apellidopa);
	}

	if(apellidomaValue === '') {
		setErrorFor(apellidoma, 'No puede dejar el Apellido Materno en blanco');
	} else {
		setSuccessFor(apellidoma);
	}


	if(telefonoValue === '') {
		setErrorFor(telefono, 'No puede dejar el Telefono en blanco');
	} else {
		setSuccessFor(telefono);
	}
	
	if(emailValue === '') {
		setErrorFor(email, 'No puede dejar el email en blanco');
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, 'No ingresó un email válido');
	} else {
		setSuccessFor(email);
	}

	if(direccionValue === '') {
		setErrorFor(direccion, 'No puede dejar el Direccion en blanco');
	} else {
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