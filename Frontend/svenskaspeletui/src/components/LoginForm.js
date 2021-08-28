import React, {useState, useEffect} from 'react'
import './../App.css'


function LoginForm({ Login, error }) {
    const [details, setDetails] = useState({username: "", password: ""});

    const submitHandler = e => {
        e.preventDefault();

        Login(details);
        
        useEffect(() => {
            fetch('/').then(response => {
                if(response.ok){
                    set
                    return response.json()
                }
            }).then(data => console.log(data))
        }, [])
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
                    
                    <input placeholder="username" type="text" name="username" id="email" onChange={e => setDetails({...details, username: e.target.value})} value={details.username} />
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
