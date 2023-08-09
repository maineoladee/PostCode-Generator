document.addEventListener("DOMContentLoaded", function() {
    const streetDropdown = document.getElementById("street");
    const postcodeGeneratorButton = document.getElementById("postcode-generator");
    const popupOverlay = document.getElementById("popup");
    const generatedPostcode = document.getElementById("generatedPostcode");

    // Initialize Select2 for the street dropdown
    $(streetDropdown).select2();

    // Listen for click event on the "Generate Postcode" button
    postcodeGeneratorButton.addEventListener("click", function() {
        const selectedStreet = streetDropdown.value;
        axios.post("/generate_postcode", { street: selectedStreet })
            .then(response => {
                showPopup(response.data);
            })
            .catch(error => console.error(error));
    });

    function generatePostcode() {
        const selectedStreet = streetDropdown.value;
        axios.post("/generate_postcode", { street: selectedStreet })
            .then(response => {
                showPopup(response.data);
            })
            .catch(error => console.error(error));
    }

    function showPopup(postcode) {
        generatedPostcode.innerText = `Generated Postcode: ${postcode}`;
        popupOverlay.style.display = "flex";
        document.addEventListener("keydown", function(event) {
            if (event.key === "Escape") {
                closePopup();
            }
        });
    }

    function closePopup() {
        popupOverlay.style.display = "none";
    }

    // Automatically close popup when clicking outside of the popup content
    window.addEventListener("click", function(event) {
        if (event.target === popupOverlay) {
            closePopup();
        }
    });
});
