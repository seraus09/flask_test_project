import info from './static/img5.png';
import ping from './static/img3.png';
import whois from './static/img2.png'
import './App.css';
import React, { Component, useState } from 'react';



export const Scroll =()=>{
    const [isShownPing, setIsShownPing] = useState(false);
    const [isShownWhois, setIsShownWhois] = useState(false);
    return(
        <div className="scroll">
            <div id="line"> 
               <img id="info" src={info} alt={"info"}  ></img>
               <p className="scroll_text">Info</p>               
                   <div id="hidden"  className="text">
                      <p>Info is useful to check IP and hostname location: IP range, ISP, organization, country, region, city, ZIP/postal code, time zone and local time.</p> 
                      <p className="p">Find out what is known about your host.</p>
                   </div>
                   
                   

            </div>
            <div className="block" id="line">
               <img id="ping"   onMouseEnter={() => setIsShownPing(true)}  onMouseLeave={() => setIsShownPing(false)} src={ping} alt={"ping"}></img>
               <p className="scroll_text">Ping</p>
               {isShownPing && (               
                   <div className="text1">
                      <p>Ping allows you to test the reachability of a host and to measure the round-trip time for messages sent from the originating host to a destination computer.</p> 
                      
                   </div>)}
            </div>
            <div className="block" id="line">
               <img id="whois" onMouseEnter={() => setIsShownWhois(true)} onMouseLeave={() => setIsShownWhois(false)}  src={whois} alt={"whois"}></img>
               <p className="scroll_text">Whois</p>
               {isShownWhois && (               
                   <div className="text2">
                      <p>Whois service allows you to quickly get all the information about domain registration, for example, the registration date and age of the domain, or find out the contacts by which you can contact the organization or person whose domain you are interested in.</p> 
                      
                   </div>)}
            </div>
           
            
        </div>
        
    )
}

export default Scroll;


