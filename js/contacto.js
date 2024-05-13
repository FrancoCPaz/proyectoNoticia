document.addEventListener("DOMContentLoaded", function() {
    // Inicializar popovers de Bootstrap
    $(function () {
        $('[data-toggle="popover"]').popover({
            trigger: 'hover' // Mostrar el popover al pasar el cursor sobre el elemento
        });
    });

    // Restringir entrada en campo de nombre
    const nameInput = document.querySelector('input[name="fullname"]');
    nameInput.addEventListener("input", function() {
        // Elimina cualquier carácter que no sea una letra o un espacio
        this.value = this.value.replace(/[^a-zA-Z\s]/g, "");
    });

    // Restringir entrada en campo de número telefónico y limitar a 12 caracteres
    const phoneInput = document.querySelector('input[name="phone"]');
    phoneInput.addEventListener("input", function() {
        // Elimina cualquier carácter que no sea + o un número
        this.value = this.value.replace(/[^+0-9]/g, "");
        
        // Limitar la longitud del número de teléfono a 12 caracteres
        if (this.value.length > 12) {
            this.value = this.value.slice(0, 12);
        }
    });

    const form = document.getElementById("contactForm");
    const modal = document.getElementById("myModal");
    const span = document.querySelector(".close");
    const confirmBtn = document.getElementById("confirmBtn");
    const cancelBtn = document.getElementById("cancelBtn");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Evita el envío del formulario por defecto
        
        // Validación de campos
        const fullname = form.querySelector('input[name="fullname"]').value.trim();
        const email = form.querySelector('input[name="email"]').value.trim();
        const phone = form.querySelector('input[name="phone"]').value.trim();
        const affair = form.querySelector('input[name="affair"]').value.trim();
        const message = form.querySelector('textarea[name="message"]').value.trim();

        // Validación de nombre
        if (fullname === "") {
            alert("Por favor, ingresa tu nombre completo.");
            return false;
        }

        // Validación de correo electrónico usando expresión regular
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert("Por favor, introduce una dirección de correo electrónico válida.");
            return false;
        }

        // Validación de número telefónico, opcional
        // Puedes implementar una validación más precisa según tus necesidades
        
        // Validación de longitud del mensaje
        if (message.length < 10) {
            alert("El mensaje debe tener al menos 10 caracteres.");
            return false;
        }

        // Si llegamos aquí, el formulario es válido
        modal.style.display = "block"; // Abre el modal de confirmación
    });

    span.addEventListener("click", function() {
        modal.style.display = "none"; // Cierra el modal al hacer clic en la "x"
    });

    window.addEventListener("click", function(event) {
        if (event.target == modal) {
            modal.style.display = "none"; // Cierra el modal al hacer clic fuera de él
        }
    });

    confirmBtn.addEventListener("click", function() {
        modal.style.display = "none"; // Cierra el modal si el usuario confirma
        form.submit(); // Envía el formulario
    });

    cancelBtn.addEventListener("click", function() {
        modal.style.display = "none"; // Cierra el modal si el usuario cancela
    });

    // Agregar evento al botón de "Más Información"
    const infoBtn = document.querySelector(".popover-button button");
    infoBtn.addEventListener("click", function() {
        // Mostrar popover con la información general de la página
        $(this).popover({
            trigger: 'manual',
            placement: 'bottom',
            title: 'Información de la Página',
            content: `
                Esta es una página de contacto que te permite enviar mensajes y contactar con nosotros. 
                Puedes ingresar tu información de contacto y el asunto del mensaje, así como escribir tu mensaje detallado en el campo correspondiente. 
                Luego, puedes hacer clic en el botón "Enviar" para enviar tu mensaje.
            `,
            html: true
        }).popover('toggle');
    });
});
