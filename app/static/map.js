function init() {
    map = new OpenLayers.Map("basicMap");
    var mapnik         = new OpenLayers.Layer.OSM();
    var fromProjection = new OpenLayers.Projection("EPSG:4326");   // Transform from WGS 1984
    var toProjection   = new OpenLayers.Projection("EPSG:900913"); // to Spherical Mercator Projection
    var position       = new OpenLayers.LonLat(-50.0059731,40.7143528).transform( fromProjection, toProjection);
    var zoom           = 10; 

    map.addLayer(mapnik);
    map.setCenter(position, zoom );
    }
    init();