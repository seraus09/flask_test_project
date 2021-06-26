import React from 'react';
import {Link} from 'react-router-dom';
import '../App.css';

export const Menu = () => {
    return(
        <nav className="menu"> 
          <Link className="link" to="/">Home</Link>
          <Link  className="link-tools" to="/tools">Tools</Link>
          <Link  className="link-log" to="/login">Login</Link>
          <Link  className="link-sig" to="/signup">Signup</Link>
        </nav>
    )
}
export default Menu;