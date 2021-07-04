import '../App.css';
import Menu from '../components/Menu.js';
import MapBasic from '../components/MapBasic'; 
import React, { useState } from 'react';
import  axios from 'axios';
import {Url} from '../config/Config.js'
import Loading from '../components/Loading';


const instance = axios.create ({
  baseURL: Url,
  headers: {
      "Content-Type": "application/json",
  } 
});

const Tools =()=>{
    const [host,setHost] = useState("")
    const [geo,setGeo] = useState([])
    const [status,setStatus] = useState(false)
    const [loading,setLoading] = useState(false)
    const [whois,setWhois] = useState([])

    async function  getApiRes(host){
       setLoading(true)
       await instance.get(`/api/geo/${host}`).then((resp) => {
          const allInfo = resp.data;
          setGeo(allInfo);
        }).then(()=> setLoading(false));
     }

    async function  getWhoisInfo(host){
      setLoading(true)
      await instance.get(`/api/whois/${host}`).then((resp) => {
         const info = resp.data;
         setWhois(info);
       }).then(()=> setLoading(false));
    }

    const handleSubmit = (evt, host) => {
        evt.preventDefault();
        getApiRes(host)
        setStatus(true)
    }
    
    const handleSubmitInfo = (evt, host) => {
        evt.preventDefault();
        getWhoisInfo(host)
        
  }
   
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
                     <button className="button_whois" type="submit" onClick={(evt) => handleSubmitInfo(evt,host)}>Whois</button>
                  </div>
                  
             </form>
        </div>
          {loading ? <div className="tools_load"><Loading/></div>: status ?
           <div className="tools_block">
                 
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

               <div className="map">
                <MapBasic latitude={geo.latitude} longitude={geo.longitude}/>
               </div>    
            </div> : null}
            <pre>{JSON.stringify(whois,null,2)}</pre>
        </body>
    )
}

export default Tools;