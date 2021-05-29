import React from 'react';
import {Link} from 'react-router-dom';
import './App.css';

export const Menu = () => {
    return(
        <div className="menu">
          <Link className="link" to = '/'>Ping-checker</Link> 
          <Link className="link-tools">Tools</Link>
          <Link className="link-log">Login</Link>
          <Link className="link-sig">Signup</Link>
        </div>
    )
}
export default Menu;