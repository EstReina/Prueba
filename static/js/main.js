const countrySelect = document.getElementById('pais');
const cityContainer = document.getElementById('city-container');
const otherCountryContainer = document.getElementById('other-country-container');

countrySelect.addEventListener('change', function() {
    const selectedCountry = countrySelect.value;

    // Mostrar ciudades si el país es Colombia
    if (selectedCountry === 'Colombia') {
        cityContainer.classList.remove('hidden');
        otherCountryContainer.classList.add('hidden'); // Oculta el campo de otro país
    } 
    // Mostrar campo de texto si el país es Otro
    else if (selectedCountry === 'Otro') {
        otherCountryContainer.classList.remove('hidden');
        cityContainer.classList.add('hidden'); // Oculta la selección de ciudades
    } 
    // Si selecciona cualquier otro país
    else {
        cityContainer.classList.add('hidden');
        otherCountryContainer.classList.add('hidden');
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


//Recoger datos del formulario y convertirlos en JSON
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Evitar el envío del formulario

    // Crear un objeto FormData para obtener los datos del formulario
    let formData = new FormData(event.target);

    // Convertir los datos del FormData a un objeto
    let formObject = {};
    formData.forEach((value, key) => {
        formObject[key] = value;
    });

    // Convertir el objeto a JSON
    let formJSON = JSON.stringify(formObject);

    // Mostrar el JSON en consola o puedes enviarlo a un servidor
    console.log(formJSON);
});