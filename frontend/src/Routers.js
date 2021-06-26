import React, { Component } from 'react';
import App from './App';
import  Tools  from './pages/Tools';
import  Login  from './pages/Login';
import Signup from './pages/Signup';
import { Route, Switch, BrowserRouter as Router,  } from 'react-router-dom'




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
