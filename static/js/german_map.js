
var map;

function initialize_german_map() {
    map = L.map( 'map', {
        center: [51.0, 9.0],
        minZoom: 6,
        zoom: 6
    });
    L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        subdomains: ['a','b','c']
    }).addTo( map );
}