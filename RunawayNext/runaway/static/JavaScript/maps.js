<<<<<<< HEAD
let req = new XMLHttpRequest();
let submit=document.getElementById("submit");
let token=document.getElementsByName("csrfmiddlewaretoken")[0];
let value=JSON.parse(document.getElementById("loc-data").textContent);
let my_obj=JSON.parse(value)
=======

let req = new XMLHttpRequest();
let submit=document.getElementById("submit");
let info=document.getElementById("info");

>>>>>>> a234bd7e1f4c6e8b44d5edfa225b37e924ed0d06
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
<<<<<<< HEAD
        center: [-94.7129, 37.0902],
        zoom: 3.2
    });
=======
        center: [-95.7129, 37.0902],
        zoom: 3
    });
    
>>>>>>> a234bd7e1f4c6e8b44d5edfa225b37e924ed0d06
        let geocoder=new MapboxGeocoder({
            accessToken: mapboxgl.accessToken,
            mapboxgl: mapboxgl,
    });
<<<<<<< HEAD
        for(let i=0; i<my_obj.length; i++){
            let lng=my_obj[i].fields.lng
            let lat=my_obj[i].fields.lat
            let description=my_obj[i].fields.description
            let pk=my_obj[i].pk
            let spots=[lng,lat]
            let el = document.createElement('div');
            el.id = 'marker';
            new mapboxgl.Marker(el)
            var popup = new mapboxgl.Popup({ offset: 25 })
                .setHTML(`
                <div id="popup">
                   <p>${description}</p></br>
                   <p><a href="../post/${pk}/">READ MORE</a></p>
                </div>
                `)
            new mapboxgl.Marker(el)
                .setLngLat(spots)
                .setPopup(popup)
                .addTo(map)    
        }           
        geocoder.on('result', function(e){
            let input = e.result.geometry.coordinates
            function place(){
                if(e.result.place_type=="poi"){
                    return e.result.text
                }
                else if(e.result.place_type=="place"){
                    return e.result.place_name
            }
        }
        console.log(place())
            submit.addEventListener("click", function(){
                new mapboxgl.Marker(el)
                var popup = new mapboxgl.Popup({ offset: 25 })
                .setHTML(`
                <div id="popup">
                    <form action="../post/create/" method="post">
                    <input type="hidden" name="csrfmiddlewaretoken" value="${token.value}">
                    <input type="hidden" name="location" value="${place()}">
                    <input type="hidden" name="lng" value="${input[0]}">
                    <input type="hidden" name="lat" value="${input[1]}">
                    <h4>${place()}</h4>
                    <p>Short description<p>
                    <input type="text" name="description">
                    <p>Add a Post!</p>
                    <textarea type="text" name="post"></textarea>
                    <button type="submit">Save</button>
                    <p><em>Marker will not save if a post is not added.</em></p>

                    </form>
                </div>`
                );              
                new mapboxgl.Marker(el)
                .setLngLat(input)
                .setPopup(popup) 
                .addTo(map) 
                
            });
            let el = document.createElement('div');
            el.id = 'marker';
            console.log(e.result.place_type)
        });
        
        map.addControl(geocoder)
        map.addControl(new mapboxgl.NavigationControl())
       
        
=======
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
>>>>>>> a234bd7e1f4c6e8b44d5edfa225b37e924ed0d06
    });
    
   
req.open("GET", "https://api.mapbox.com/geocoding/v5/mapbox.places/portland.json?access_token=pk.eyJ1IjoibWthdDkwIiwiYSI6ImNqd3FueDh2YzAwb3c0YXQ5cHliMGNhOW0ifQ.PEpXT5nwgTV6Xx77jf8dRg");
req.setRequestHeader("Authorization", 'Token token="pk.eyJ1IjoibWthdDkwIiwiYSI6ImNqd3FueDh2YzAwb3c0YXQ5cHliMGNhOW0ifQ.PEpXT5nwgTV6Xx77jf8dRg"');
req.send()
