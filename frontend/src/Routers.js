import React, { Component } from 'react';
import App from './App';
import  Tools  from './Tools';
import  Login  from './Login';
import { Route, Switch, BrowserRouter as Router,  } from 'react-router-dom'
import Signup from './Signup';



export const Routers = ()=> {
    return (
    <Router>
        <Switch>
            <Route exact path="/" component={App} />
            <Route exact path="/tools" component={Tools}/>
            <Route exact path="/login" component={Login}/>
            <Route exact path="/signup" component={Signup}/>
        </Switch>
    </Router>)
}
