import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import './App.css';
import Home from './components/pages/Home';
import Login from './components/pages/Login';
import Leaderboard from './components/pages/Leaderboard';
import Add from './components/pages/Add';



function App() {

  // function sayHello(){
  //   alert("Hello! Soon you can log in here")
  // }
  return (
    <>
    <Router>
      <Switch>
        <Route path='/' exact component={Home} />
        <Route path='/login' component={Login} />
        <Route path='/leaderboard' component={Leaderboard} />
        <Route path='/add' component={Add} />
      </Switch>
    </Router>
  </>
  );
}

export default App;
