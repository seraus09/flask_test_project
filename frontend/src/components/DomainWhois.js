import '../App.css';
import axios from 'axios';
import {Url} from '../config/Config.js'
import { useState, useEffect } from 'react';
import Loading from '../components/Loading';

const instance = axios.create ({
    baseURL: Url,
    headers: {
        "Content-Type": "application/json",
    } 
  });

const DomainWhois = (props) => {
  
  const [whois,setWhois] = useState([])
  const [loading,setLoading] = useState(false)
  
  async function  getApiRes(host){
    setLoading(true)
    await instance.get(`/api/whois/${props.host}`).then((resp) => {
       const allInfo = resp.data;
       setWhois(allInfo);
     }).then(()=> setLoading(false))
     .catch(error => {
       alert(error)

   });
  }
  useEffect(() => {
      getApiRes(props.host)
      },[props.host]);
      
      console.log(typeof(whois))
 
      return(
        
        loading ? <div className="tools_load"><Loading/></div>:
        <div className="tools_block">
        <table className="table">
          <tbody>    
            <tr>
              <td>Name:</td>
              <td>{whois.main_data.name}</td>
            </tr>
            <tr>
              <td>Registrar:</td>
              <td>{whois.main_data.registrar}</td>
            </tr>
            <tr>
              <td>Registrant country:</td>
              <td>{whois.main_data.registrant_country}</td>
            </tr>
            <tr>
              <td>Creation date:</td>
              <td>{whois.time_data.creation_date}</td>
            </tr>
            <tr>
              <td>Expiration date:</td>
              <td>{whois.time_data.expiration_date}</td>
            </tr>
            <tr>
              <td>Last update:</td>
              <td>{whois.time_data.last_updated}</td>
            </tr>
              <tr>
               <td>Status:</td>
              <td>{whois.main_data.status}</td>
            </tr>
            <tr>
              <td>Statuses:</td>
              <td>{whois.main_data.statuses}</td>
            </tr>
            <tr>
              <td>DNSsec:</td>
              <td>{whois.main_data.dnssec}</td>
            </tr>
            <tr>
              <td>Name servers:</td>
              <td>{whois.time_data.name_servers}</td>
            </tr>

            </tbody>
          </table>
        
        </div>
        
      )
    }

export default DomainWhois;