
document.addEventListener("DOMContentLoaded", function() {
    // Inicializar popovers de Bootstrap
    $(function () {
        $('[data-toggle="popover"]').popover({
            trigger: 'hover' // Mostrar el popover al pasar el cursor sobre el elemento
        });
    });

    // Restringir entrada en campo de número telefónico
    const phoneInput = document.querySelector('input[name="phone"]');
    phoneInput.addEventListener("input", function() {
        // Elimina cualquier carácter que no sea + o un número
        this.value = this.value.replace(/[^+0-9]/g, "");
    });

    const form = document.getElementById("contactForm");
    const modal = document.getElementById("myModal");
    const span = document.querySelector(".close");
    const confirmBtn = document.getElementById("confirmBtn");
    const cancelBtn = document.getElementById("cancelBtn");

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Evita el envío del formulario por defecto
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
