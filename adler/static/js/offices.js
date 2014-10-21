/*! adler-m v0.0.0, 2014-08-07 */
$(function(){var offices=eval($("#officesData").text()),$officesMap=$("#offices-map"),mapBounds={minLat:32e3,minLon:32e3,maxLat:0,maxLon:0},firstOffice,firstScreenOfficesCount=0;for(var i in offices){var office=offices[i];if(office.showImmediate){var coords=office.map.latlng.split(","),lat=parseFloat(coords[0]),lon=parseFloat(coords[1]);lat>mapBounds.maxLat&&(mapBounds.maxLat=lat),lat<mapBounds.minLat&&(mapBounds.minLat=lat),lon>mapBounds.maxLon&&(mapBounds.maxLon=lon),lon<mapBounds.minLon&&(mapBounds.minLon=lon),firstOffice||(firstOffice=office),firstScreenOfficesCount++}}ymaps.ready(function(){var a=new ymaps.Map($officesMap[0],ymaps.util.bounds.getCenterAndZoom([[mapBounds.minLat,mapBounds.minLon],[mapBounds.maxLat,mapBounds.maxLon]],[$officesMap.width(),$officesMap.height()]));if(1>=firstScreenOfficesCount){var b=firstOffice.map.latlng.split(",");a.setCenter(b,firstOffice.map.zoom)}for(var c in offices){var d=offices[c],e=d.map.latlng.split(","),f=new ymaps.Placemark(e,{content:d.name,balloonContent:"<h5>"+d.name+"</h5>"});a.geoObjects.add(f)}$(".show-on-map").click(function(b){b.preventDefault();var c=offices[parseInt($(this).data("office"))],d=c.map.latlng.split(",");a.setCenter(d,c.map.zoom)})})});