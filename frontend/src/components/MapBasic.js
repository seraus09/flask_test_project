import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet'
import L from 'leaflet'
import "./index.css"
import "leaflet/dist/leaflet.css"
import { useState } from 'react';

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png').default,
  iconUrl: require('leaflet/dist/images/marker-icon.png').default,
  shadowUrl: require('leaflet/dist/images/marker-shadow.png').default,
});



const MapBasic =(props)=>{
    const [position,setPosition] = useState([props?.latitude.toFixed(4),props?.longitude.toFixed(4)])
    return(
      <div className="leaflet-container">
      <MapContainer center={position} zoom={5} scrollWheelZoom={false}>
      <TileLayer
        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={position}>
      </Marker>
    </MapContainer>
    </div>
  )
}

export default MapBasic;