import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import './App.css';
import Home from './components/pages/Home';
import Login from './components/pages/Login';
import Leaderboard from './components/pages/Leaderboard';
import Add from './components/pages/Add';
import UserStore from './stores/UserStore';

class App extends React.Component {

  async componentDidMount() {

    try {
      let res = await fetch('/isLoggedIn', {
        method: 'post',
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json'
        }
      });
      let result = await res.json();
      if (result && result.sucess) {
        UserStore.loading = false;
        UserStore.isLoggedIn = true;
        UserStore.username = result.username;
      }
      else{
        UserStore.loading = true;
        UserStore.isLoggedIn = false;
      }
    }
    catch(e) {
      UserStore.loading = false;
        UserStore.isLoggedIn = false;
    }
  }

  async doLogout() {

    try {
      let res = await fetch('/logout', {
        method: 'post',
        headers: {
          'Accept': 'application/json',
          'Content-type': 'application/json'
        }
      });
      let result = await res.json();
      if (result && result.sucess) {
        UserStore.isLoggedIn = false;
        UserStore.username = '';
      }
    }
    catch(e) {
        console.log(e)
    }
  }

  render() {
    if(UserStore.loading) {
      return(
        
      )
    }
    return(
      <Router>
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/login' component={Login} />
          <Route path='/leaderboard' component={Leaderboard} />
          <Route path='/add' component={Add} />
        </Switch>
      </Router>
    );
  }
}

export default App;

