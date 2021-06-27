import '../App.css';
import Menu from '../components/Menu.js';
import MapBasic from '../components/MapBasic'; 




const Tools =()=>{
    return(
        <body>
        <header className="tools_header">
            <Menu/>
        </header>
        <div>
            <form >
                  <input className="input" type="text" placeholder="Enter IP or domain"/>
                  <div>
                     <button type="submit">Info</button>
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