const countrySelect = document.getElementById('pais');
const cityContainer = document.getElementById('city-container');

countrySelect.addEventListener('change', function() {
    const selectedCountry = countrySelect.value;

    // Mostrar ciudades si el país es Colombia
    if (selectedCountry === 'Colombia') {
        cityContainer.classList.remove('hidden');
        
    } 
    // Mostrar campo de texto si el país es Otro
    else if (selectedCountry === 'Otro') {
        cityContainer.classList.add('hidden'); // Oculta la selección de ciudades
    } 
    // Si selecciona cualquier otro país
    else {
        cityContainer.classList.add('hidden');
    }
});


//Delvolverse al inicio de la página

document.getElementById('inicio').addEventListener('click', function(event) {
    event.preventDefault(); // Evita el comportamiento predeterminado del enlace
    window.scrollTo({
        top: 0,
        behavior: 'smooth' // Desplazamiento suave
    });
});
