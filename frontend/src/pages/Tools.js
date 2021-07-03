import '../App.css';
import Menu from '../components/Menu.js';
import MapBasic from '../components/MapBasic'; 
import React, { useState } from 'react';
import  axios from 'axios';




const Tools =()=>{
    const [host,setHost] = useState("")
    const [geo,setGeo] = useState([])
    const [status,setStatus] = useState(false)
    const [loading,setLoading] = useState(false)
    
    async function  getApiRes(host){
       const apiUrl = `http://127.0.0.1:5000/api/geo/${host}`;
       setLoading(true)
       await axios.get(apiUrl).then((resp) => {
          const allInfo = resp.data;
          setGeo(allInfo);
          console.log(allInfo)
        }).then(()=> setLoading(false));
     }

     
     const handleSubmit = (evt, host) => {
        evt.preventDefault();
        getApiRes(host)
        setStatus(true)
    }
    
    console.log(host)
   
    return(
        <body>
        <header className="tools_header">
            <Menu/>
        </header>
        <div>
            <form >
                  <input className="input" onChange={e => setHost(e.target.value)}   value={host} type="text" placeholder="Enter IP or domain"/>
                  <div>
                     <button type="submit" onClick={(evt) => handleSubmit(evt,host)} >Info</button>
                     <button className="button_ping" type="submit">Ping</button>
                     <button className="button_whois" type="submit">Whois</button>
                  </div>
                  
             </form>
        </div>
        <div className="tools_block">
           <div>
                {loading ? null: status ? 
                   <table className="table">
                   <tbody>    
                    <tr>
                      <td>IP-address:</td>
                      <td>{geo.ip}</td>
                    </tr>
                    <tr>
                      <td>Type:</td>
                      <td>{geo.type}</td>
                    </tr>
                    <tr>
                      <td>Continent:</td>
                      <td>{geo.continent_name}</td>
                    </tr>
                    <tr>
                      <td>Country code:</td>
                      <td>{geo.country_code}</td>
                    </tr>
                    <tr>
                      <td>Country:</td>
                      <td>{geo.country_name}  <img style={{width: '15px', height: '15px'}} src={geo.location.country_flag}></img></td>
                    </tr>
                    <tr>
                      <td>Capital:</td>
                      <td>{geo.location.capital}</td>
                    </tr>
                    <tr>
                      <td>Region:</td>
                      <td>{geo.region_name}</td>
                    </tr>
                    <tr>
                      <td>City:</td>
                      <td>{geo.city}</td>
                    </tr>
                    <tr>
                      <td>ZIP:</td>
                      <td>{geo.zip}</td>
                    </tr>

                    </tbody>
                   </table>
                   : null}
                
            </div>
            <div className="map">
            {loading ? null: status ? <MapBasic latitude={geo.latitude} longitude={geo.longitude}/> : null}
            </div>
        </div>
        </body>
    )
}

export default Tools;