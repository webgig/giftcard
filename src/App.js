import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import LoginPage from './components/Login';
import { PrivateRoute } from './components/PrivateRoute';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { HomePage } from './components/HomePage';

class App extends Component {
  render() {
    return (
        <Router>
            <div>
                <PrivateRoute exact path="/" component={HomePage} />
                <Route path="/login" component={LoginPage} />
            </div>
        </Router>
    );
  }
}

export default App;
