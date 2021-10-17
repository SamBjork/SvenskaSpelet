import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import "./App.css";
import Home from "./components/pages/Home";
import Login from "./components/pages/Login";
import Leaderboard from "./components/pages/Leaderboard";
import Add from "./components/pages/Add";
import Game from "./components/pages/Game";
import UserStore from "./stores/UserStore";

class App extends React.Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/login" component={Login} />
          <Route path="/leaderboard" component={Leaderboard} />
          <Route path="/add" component={Add} />
          <Route path="/game" component={Game} />
        </Switch>
      </Router>
    );
  }
}

export default App;
