import React, {useRef, useState } from 'react';
import {Link}from 'react-router-dom'
import '../../App.css';
import logo from './../../assets/ssr.png';
import { Button } from '../Button';
import LoginForm from '../../components/LoginForm';




function Home() {

    const [user, setUser] = useState({username: ""});
    const [login, setLogin] = useState({isLoggedin: false})
    const [error, setError] = useState("");

const OpenLogin = () => {
        setLogin(true)
    }

const Login = details => {

    setLogin(true)
    console.log(details)

    if (this.state )
    {
        setUser({
            username: details.username,
            password: details.password
        })
        setLogin(false)
    }

    else{
        setError("Användarnamn och lösenord stämmer inte!")
    }

}

const Logout = () => {
    setUser({
        username: "",
        password: ""
    })
}




    return(

        <div className="App">
            <header className="App-header">
                <img src={logo} id="App-logo" alt="logo" />
                <br/>
                Välkommen till
                <br/>
                "Svenska Spelet"
            {(user.username != "") ? (
                <div className="welcome">
                    <h2>Välkommen, <span>{user.username}</span></h2>
                    <button onClick={Logout}>Logga ut</button>
                    <button>Spela</button>
                </div>
            ) : (
                ""
                    
            )}
            {(login.isLoggedin != false) ? (
                <LoginForm Login={Login} error={error}/>
            ) : (
                <Button onClick={OpenLogin}>
                Logga in
                </Button>  
            )}
                
                <Link to="/register">
                <Button>
                Registera dig
                </Button>
                </Link>
                <Link to="/leaderboard">
                <Button>
                Se topplistan
                </Button>
                </Link>
            </header>
            </div>
        )
    }
    export default Home;