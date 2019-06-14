
let req = new XMLHttpRequest();
let submit=document.getElementById("submit");
let info=document.getElementById("info");

    req.addEventListener("progress", function(e) {
    });
    req.addEventListener("error", function(e) {
        target.innerText = "Error. Please Try Again.";
    });
    req.addEventListener("load", function(e) {
        let response = JSON.parse(req.responseText); 
        mapboxgl.accessToken = 'pk.eyJ1IjoibWthdDkwIiwiYSI6ImNqd3FueDh2YzAwb3c0YXQ5cHliMGNhOW0ifQ.PEpXT5nwgTV6Xx77jf8dRg';
        let map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/streets-v9',
        center: [-95.7129, 37.0902],
        zoom: 3
    });
    
        let geocoder=new MapboxGeocoder({
            accessToken: mapboxgl.accessToken,
            mapboxgl: mapboxgl,
    });
        geocoder.on('result', function(e){
            let input = e.result.geometry.coordinates
            submit.addEventListener("click", function(){
                new mapboxgl.Marker(el)
                .setLngLat(input)
                .addTo(map);
                var popup = new mapboxgl.Popup({ offset: 25 })
                .setHTML(`<div id="popup"><p>This is where short info will be.</p><a href="">Read More</a></br><button type="submit" id="sub">Add info</button><button type="submit" id="edit">Edit</button><button type="submit" id="delete">Delete</button></div>`);                
                new mapboxgl.Marker(el)
                .setLngLat(input)
                .setPopup(popup) 
                .addTo(map);           
            });
            
            var el = document.createElement('div');
            el.id = 'marker';
        });
       
        map.addControl(geocoder)
        map.addControl(new mapboxgl.NavigationControl());  
    });
    
   
req.open("GET", "https://api.mapbox.com/geocoding/v5/mapbox.places/portland.json?access_token=pk.eyJ1IjoibWthdDkwIiwiYSI6ImNqd3FueDh2YzAwb3c0YXQ5cHliMGNhOW0ifQ.PEpXT5nwgTV6Xx77jf8dRg");
req.setRequestHeader("Authorization", 'Token token="pk.eyJ1IjoibWthdDkwIiwiYSI6ImNqd3FueDh2YzAwb3c0YXQ5cHliMGNhOW0ifQ.PEpXT5nwgTV6Xx77jf8dRg"');
req.send()
