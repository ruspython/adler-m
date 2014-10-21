$(function(){
    var offices = eval($('#officesData').text()),
        $officesMap = $('#offices-map'),
        mapBounds = {
            minLat: 32000,
            minLon: 32000,
            maxLat: 0,
            maxLon: 0
        },
        firstOffice,
        firstScreenOfficesCount = 0
    for(var i in offices){
        var office = offices[i];
        if(office.showImmediate){
            var coords = office.map.latlng.split(','),
                lat = parseFloat(coords[0]),
                lon = parseFloat(coords[1])
            if(lat > mapBounds.maxLat) mapBounds.maxLat = lat;
            if(lat < mapBounds.minLat) mapBounds.minLat = lat;
            if(lon > mapBounds.maxLon) mapBounds.maxLon = lon;
            if(lon < mapBounds.minLon) mapBounds.minLon = lon;
            if(!firstOffice) firstOffice = office;
            firstScreenOfficesCount++;
        }
    }
    ymaps.ready(function(){
        var officesMap = new ymaps.Map(
            $officesMap[0],
            ymaps.util.bounds.getCenterAndZoom(
                [[mapBounds.minLat, mapBounds.minLon], [mapBounds.maxLat, mapBounds.maxLon]],
                [$officesMap.width(), $officesMap.height()]
            )
        );
        if(firstScreenOfficesCount<=1){
            var firstOfficeCoords = firstOffice.map.latlng.split(',');
            officesMap.setCenter(firstOfficeCoords, firstOffice.map.zoom);
        }
        for(var i in offices){
            var office = offices[i],
                coords = office.map.latlng.split(','),
                officePlacemark = new ymaps.Placemark(
                    coords,
                    {
                        content: office.name,
                        balloonContent: '<h5>'+office.name+'</h5>'
                    }
                );
            officesMap.geoObjects.add(officePlacemark);
        }
        $('.show-on-map').click(function(e){
            e.preventDefault();
            var office = offices[parseInt($(this).data('office'))],
                coords = office.map.latlng.split(',');
            officesMap.setCenter(coords, office.map.zoom);
        })
    });
});