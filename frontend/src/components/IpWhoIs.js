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

const IpWhois = (props) => {
   
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
        },[props.evt]);
      
    

      return(
        loading ? <div className="tools_load"><Loading/></div>:
        <div className="tools_block">
          <table className="table">
          <tbody>    
            <tr>
              <td>CIDR:</td>
              <td>{whois.cidr}</td>
            </tr>
            <tr>
              <td>Name:</td>
              <td>{whois.name}</td>
            </tr>
            <tr>
              <td>Handle:</td>
              <td>{whois.handle}</td>
            </tr>
            <tr>
              <td>Range:</td>
              <td>{whois.range}</td>
            </tr>
            <tr>
              <td>Description:</td>
              <td>{whois.description}</td>
            </tr>
            <tr>
              <td>Country:</td>
              <td>{whois.country}</td>
            </tr>
              <tr>
               <td>State:</td>
              <td>{whois.state}</td>
            </tr>
            <tr>
              <td>City:</td>
              <td>{whois.city}</td>
            </tr>
            <tr>
              <td>Address:</td>
              <td>{whois.address}</td>
            </tr>
            <tr>
              <td>Emails:</td>
              <td>{whois.emails}</td>
            </tr>
            <tr>
              <td>Created:</td>
              <td>{whois.created}</td>
            </tr>
            <tr>
              <td>Updated:</td>
              <td>{whois.updated}</td>
            </tr>

            </tbody>
          </table>

        </div>
      )
      }

export default IpWhois;