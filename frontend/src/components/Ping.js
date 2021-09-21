import '../App.css';
import axios from 'axios';
import {Node1} from '../config/Config.js'
import { useState, useEffect } from 'react';


const instance = axios.create ({
    baseURL: Node1,
    headers: {
        "Content-Type": "application/json",
    } 
  });

const Ping = (props) => {
  
  const [pingCount,setPingCount] = useState([])
  const [loading,setLoading] = useState(false)
  
  async function  getApiRes(){
    setLoading(true)
    await instance.get(`/api/v1.0/tasks/${props.host}`).then((resp) => {
       const allInfo = resp.data;
       setPingCount(allInfo);
     }).then(()=> setLoading(false))
     .catch(error => {
       alert(error)

   });
  }
  
  useEffect(() => {
      getApiRes(props.host)
      },[props.host]);
 
      return(
        <div className="tools_block">
        <table className="table">
          <tbody>    
            <tr>
              <td>Node1:</td>
              <td>{pingCount?.packet}/4</td>
            </tr>
            </tbody>
          </table>
        
        </div>
      )
      
    }

export default Ping;