
var german_map;

function initialize_german_map() {
    german_map = L.map( 'map', {
        center: [51.0, 9.0],
        //,
        //minZoom: 6,
        zoom: 6
    });
    L.tileLayer( 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>',
        subdomains: ['a','b','c']
    }).addTo(german_map);
    let marker = L.marker([50.7359, 7.10066],
        {
	color: 'red',
	fillColor: '#f03',
	fillOpacity: 0.5,
	radius: 500
});
    marker.addTo(german_map);
}

function mark_city(lng, lat) {
    console.log(lng +" "+ lat);
    marker = L.marker([lat, lng]).addTo(german_map);
}