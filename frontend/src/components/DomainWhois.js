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
  
  async function  getApiRes(){
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
 
      return(
        
        loading ? <div className="tools_load"><Loading/></div>:
        <div className="tools_block">
        <table className="table">
          <tbody>    
            <tr>
              <td>Name:</td>
              <td>{whois?.main_data?.name}</td>
            </tr>
            <tr>
              <td>Registrar:</td>
              <td>{whois?.main_data?.registrar}</td>
            </tr>
            <tr>
              <td>Registrant country:</td>
              <td>{whois?.main_data?.registrant_country}</td>
            </tr>
            <tr>
              <td>Creation date:</td>
              <td>{whois?.data?.creation_date}</td>
            </tr>
            <tr>
              <td>Expiration date:</td>
              <td>{whois?.data?.expiration_date}</td>
            </tr>
            <tr>
              <td>Last update:</td>
              <td>{whois?.data?.last_updated}</td>
            </tr>
              <tr>
               <td>Status:</td>
              <td>{whois?.main_data?.status}</td>
            </tr>
            <tr>
              <td>Statuses:</td>
              <td>{whois?.main_data?.statuses}</td>
            </tr>
            <tr>
              <td>Name servers:</td>
              <td>{whois?.data?.name_servers}</td>
            </tr>

            </tbody>
          </table>
        
        </div>
      )
      
    }

export default DomainWhois;