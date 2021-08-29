import React, {useState, useEffect} from 'react'
import './../App.css'
import axios from 'axios'


function LoginForm({ Login, error }) {
    const [details, setDetails] = useState({username: "", password: ""});

    const submitHandler = e => {
        e.preventDefault();

        Login(details);

        let formData = new FormData();    //formdata object

        formData.append('username', details.username);   //append the values with key, value pair
        formData.append('password', details.password);

        const config = {     
            headers: { 'content-type': 'multipart/form-data' }
        }

        axios.post('http://127.0.0.1:5000/login', formData, config)
            .then(response => {
                console.log(response)
                return '/register'
            })
            .catch(error => {
                console.log(error)
                return 403
            })

        // useEffect(() => {
        //     fetch('/login').then(response => {
        //         if(response.ok){
        //             set
        //             return response.json()
        //         }
        //         else{
        //             return 403
        //         }
        //     }).then(data => console.log(data))
        // }, [])
    }
    

    return (
        <>
        <div className="text">Vänligen logga in eller skapa ett konto!</div>
        <form onSubmit={submitHandler}>
            <div className="form-inner">
                <div className="form-group">
                    {(error != "") ? (
                        <div style={{color: "red"}} className="error">{error}</div> 
                    ) : ""}
                    
                    <input placeholder="användarnamn" type="text" name="username" id="username" onChange={e => setDetails({...details, username: e.target.value})} value={details.username} />
                </div>
                <div className="form-group">
                    <input placeholder="lösenord" type="password" name="password" id="password" onChange={e => setDetails({...details, password: e.target.value})} value={details.password} />
                </div>
                <input type="submit" value="Logga in" />
            </div>
        </form>
    </>
    )
}

export default LoginForm
