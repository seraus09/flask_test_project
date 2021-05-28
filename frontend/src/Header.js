import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import App from './App';

const Router = ReactRouterDOM.BrowserRouter;
const Route = ReactRouterDOM.Route;
const Switch = ReactRouterDOM.Switch;

export default class About extends Component{
    render(){
        return <h2>О сайте</h2>;
    }
}

ReactDOM.render(
    <Router>
        <Switch>
            <Route exact path="/" component={App} />
            <Route path="/about" component={About} />
            <Route component={NotFound} />
        </Switch>
    </Router>,
    
)
