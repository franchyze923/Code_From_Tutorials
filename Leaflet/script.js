const auth_user = 'https://www.strava.com/oauth/authorize?client_id=32172&redirect_uri=http://localhost&response_type=code&scope=activity:read';
const auth_link = 'https://www.strava.com/oauth/token';

  function getActivites(code) {
    const activites_link = `https://www.strava.com/api/v3/athlete/activities?access_token=${code.access_token}`
    console.log(code)
    fetch(activites_link)
        .then((res) => res.json())
        //.then(res => console.log(res));
        .then(function (data) {
  

            var mymap = L.map('mapid').setView([38.895417, -77.033616], 11);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(mymap);
        
            var run_color = "red";
     
        
            for (var x = 0; x < data.length; x++) {
              
              var act_id = data[x].id;
              console.log(act_id);
              console.log(data[x])
              console.log(data[x].map.summary_polyline)
              var coordinates = L.Polyline.fromEncoded(data[x].map.summary_polyline).getLatLngs();
        
        
              L.polyline(
                coordinates,
                {
                  color: "green",
                  weight: 5,
                  opacity: .7,
                  lineJoin: 'round'
        
                }
              ).addTo(mymap);
            }
          })
 
  }
  
  function reAuthorize() {
    fetch(auth_link, {
        method: 'post',
  
        headers: {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
  
            client_id: '32172',
            client_secret: 'c9dac208d0c515b6e8915afb92ffbccfb1630f71',
            refresh_token: 'f6a3dd6e1e2dad06db03fe04ec88485fc4fa79c8',
            grant_type: 'refresh_token'
  
        })
  
    }).then(res => res.json())
        .then(res => getActivites(res))
  }
  
  reAuthorize()