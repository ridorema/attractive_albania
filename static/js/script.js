// Initialize the map
var map = L.map('map').setView([41.3275, 19.8189], 8); // Centered on Albania

// Add a tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Function to show map with markers
function showMap(type) {
    fetch(`/sites/${type}`)
        .then(response => response.json())
        .then(sites => {
            // Remove existing markers
            map.eachLayer(function (layer) {
                if (layer instanceof L.Marker) {
                    map.removeLayer(layer);
                }
            });

            // Add new markers
            sites.forEach(function(site) {
                var marker = L.marker([site.lat, site.lng]).addTo(map)
                    .bindPopup(`<b>${site.name}</b><br><a href="/site/${site.id}">More info</a>`);
            });
        });
}
// Open the login modal
function openLoginModal() {
    document.getElementById("loginModal").style.display = "block";
}

// Close the login modal
function closeLoginModal() {
    document.getElementById("loginModal").style.display = "none";
}

// Open the create account modal
function openCreateAccountModal() {
    document.getElementById("createAccountModal").style.display = "block";
}

// Close the create account modal
function closeCreateAccountModal() {
    document.getElementById("createAccountModal").style.display = "none";
}


// Show historical sites by default
showMap('historical');
