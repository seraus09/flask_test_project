import '../App.css';
import Menu from '../components/Menu.js';
import MapBasic from '../components/MapBasic'; 
import React, { useState } from 'react';
import  axios from 'axios';
import {Url} from '../config/Config.js'
import Loading from '../components/Loading';
import IpWhois from '../components/IpWhoIs';
import DomainWhois from '../components/DomainWhois'




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
    const [ipWhois,setIpWhois] = useState(false)
    const [domWhois,setDomWhois] = useState(false)
    const [isValid, setIsValid] = useState(false);
    const [inputError, setInputError] = useState('')
    const [WhoisIPdata, setWhoisIPdata] = useState([])
    const [WhoisDomainData, setWhoisDomainData] = useState([])

    async function  getApiRes(host){
       setLoading(true)
       await instance.get(`/api/geo/${host}`).then((resp) => {
          const allInfo = resp.data;
          setGeo(allInfo);
        }).then(()=> setLoading(false))
        .catch(error => {
          alert(error)

      });
     }

   
    const handleSubmit = (evt, host) => {
        evt.preventDefault();
        const re = /^(?:(?:(?:[a-zA-z\-]+)\:\/{1,3})?(?:[a-zA-Z0-9])(?:[a-zA-Z0-9\-\.]){1,61}(?:\.[a-zA-Z]{2,})+|\[(?:(?:(?:[a-fA-F0-9]){1,4})(?::(?:[a-fA-F0-9]){1,4}){7}|::1|::)\]|(?:(?:[0-9]{1,3})(?:\.[0-9]{1,3}){3}))(?:\:[0-9]{1,5})?$/
        if (!re.test(String(host).toLowerCase())){
          setIsValid(true) || setInputError("Please type correct IP-address or domain")
          setTimeout(() => {setInputError("")}, 5000)
          if(host.length < 4){
            setIsValid(true) || setInputError("Please type correct IP-address or domain")
            setTimeout(() => {setInputError("")}, 5000)
          }
        }
         
        else{
            getApiRes(host)
            setStatus(true)
          }
    }
    
    const handleSubmitInfo = (evt,host) => {
        evt.preventDefault();
        const re_ip = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/
        const re_domain = /\b((?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}\b/

        if (re_ip.test(String(host).toLowerCase())){
          setWhoisIPdata(<IpWhois host={host}/>)
          setIpWhois(true)
          setStatus(false)
          setDomWhois(false)
          } else if (re_domain.test(String(host).toLowerCase())){
              setWhoisDomainData(<DomainWhois host={host}/>)
              setDomWhois(true)
              setStatus(false)
              setIpWhois(false)
              
            }
        else{
            setIsValid(true) || setInputError("Please type correct IP-address or domain")
            setTimeout(() => {setInputError("")}, 5000)
        }
      }
 
   
    return(
        <body>
        <header className="tools_header">
            <Menu/>
        </header>
        <div>
            <form >
                   {(isValid && inputError) && <div className="error_msg">{inputError}</div>}
                  <input className="input" onChange={e => setHost(e.target.value)}   value={host} type="text" name="field" placeholder="Enter IP or domain"/>
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
            </div> : domWhois ? WhoisDomainData  : !domWhois && ipWhois ? WhoisIPdata: null }
        </body>
    )
}

export default Tools;