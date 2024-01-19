function iniciarCarga() {
    var barraDeCargaContainer = document.getElementById("barraDeCargaContainer");
    var barraDeCarga = document.getElementById("barraDeCarga");

    // Mostrar la barra de carga
    barraDeCargaContainer.style.display = "block";

    setTimeout(function() {
        // Ocultar el elemento
        barraDeCargaContainer.style.display = "none";
    }, 3000);

    setTimeout(function() {
        window.location.href = '/';
    }, 5000);
        
                
}

