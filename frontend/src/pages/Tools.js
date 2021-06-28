import '../App.css';
import Menu from '../components/Menu.js';
import MapBasic from '../components/MapBasic'; 
import React, { useState } from 'react';



const Tools =()=>{
    const [host,setHost] = useState("")
    
    const handleSubmit = (evt) => {
        evt.preventDefault();
        alert(`Submitting host ${host}`)
    }
    

    console.log(host)
    
   
    return(
        <body>
        <header className="tools_header">
            <Menu/>
        </header>
        <div>
            <form >
                  <input className="input" onChange={e => setHost(e.target.value)}  value={host} type="text" placeholder="Enter IP or domain"/>
                  <div>
                     <button type="submit" onClick={handleSubmit}>Info</button>
                     <button className="button_ping" type="submit">Ping</button>
                     <button className="button_whois" type="submit">Whois</button>
                  </div>
             </form>
        </div>
           <div className="map"> 
            <MapBasic/>
            </div>   
        </body>
    )
}

export default Tools;