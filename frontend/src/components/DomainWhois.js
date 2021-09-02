import './index.css'
import axios from 'axios';
import {Url} from '../config/Config.js'
import { useState, useEffect } from 'react';

const instance = axios.create ({
    baseURL: Url,
    headers: {
        "Content-Type": "application/json",
    } 
  });

const DomainWhois = (props) => {
   
    const [whois,setWhois] = useState([])
    
    useEffect(() => {
        instance.get(`/api/whois/${props.host}`).then((resp) => {
           const info = resp.data;
           setWhois(info);
         }).catch(error => {
          alert(error) 
          })
        },[props.host]);
      
    

      return(
        <pre>{JSON.stringify(whois,null,2)}</pre>
      )
    

}

export default DomainWhois;