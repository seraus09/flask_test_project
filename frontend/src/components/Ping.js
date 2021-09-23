import '../App.css'
import './index.scss'
import axios from 'axios';
import {Node1, Node2} from '../config/Config.js'
import { useState, useEffect } from 'react'
import Loader from 'react-loaders'


const instance = axios.create ({
    baseURL: Node1,
    headers: {
        "Content-Type": "application/json",
    } 
  });

const instanceNode2 = axios.create ({
    baseURL: Node2,
    headers: {
        "Content-Type": "application/json",
    } 
  });  

const Ping = (props) => {
  
  const [pingCountNode1,setPingCountNode1] = useState([])
  const [pingCountNode2,setPingCountNode2] = useState([])
  const [loading,setLoading] = useState(false)
  const [loadingNode2,setLoadingNode2] = useState(false)
 
  let colorName = "green"
  let load = <Loader type="ball-pulse-sync"/>
  

  async function  getResNode1(){
    setLoadingNode2(true)
    await instance.get(`/api/v1.0/tasks/${props.host}`).then((resp) => {
       const allInfo = resp.data;
       setPingCountNode1(allInfo);
     }).then(()=> setLoadingNode2(false))
     .catch(error => {
   });
  }
 
  async function  getResNode2(){
    setLoading(true)
    await instanceNode2.get(`/api/v1.0/tasks/${props.host}`).then((resp) => {
       const allInfo = resp.data;
       setPingCountNode2(allInfo);
     }).then(()=> setLoading(false))
     .catch(error => {
       alert(error)

   });
  }

  useEffect(() => {
      getResNode1(props.host)
      getResNode2(props.host)
  }, [props.evt])

  
  
 
  
      return(
        <div className="tools_block">
        <table className="table">
          <tbody>    
            <tr>
              <td className>Node1:</td>
              <td className={"ping_style"}>{loadingNode2 ?  load: (<div className={colorName}>{pingCountNode1?.packet}/4</div>)}</td>
            </tr>
            <tr>
              <td> Node2:</td>
              <td>{loading ? load:  (<div className={colorName}>{pingCountNode2?.packet}/4</div>)}</td>
            </tr>
            </tbody>
          </table>
        
        </div>
      )
      
    }

export default Ping;