import React, { Component } from 'react';
import App from './App';
import { Route, Switch, BrowserRouter as Router,  } from 'react-router-dom'



export const Routers = ()=> {
    return (
    <Router>
        <Switch>
            <Route exact path="/" component={App} />
        </Switch>
    </Router>)
}
