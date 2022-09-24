
import React, { useState, useEffect } from 'react'
import APIService from '../Component/APIService';



function Login() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('')

    const [isLogin, setLogin] = useState(true)
    const [token, setToken] = useState([])

    const loginBtn1 = () => {
        APIService.LoginUser({ username, password })
            .then(resp => setToken(resp.auth_token))
            .catch(error => console.log(error))
    }

  
    const loginBtn = () => {
        APIService.LoginUser({username, password})
            .then(resp => localStorage.setItem('auth_token', resp.auth_token), resp => localStorage.setItem('InLogin', true))
            .catch(error => console.log(error))
        console.log(localStorage.getItem('auth_token'))
    }

    const RegisterBtn = () => {
        APIService.RegisterUser({ email, username, password })
            .then(resp => console.log(resp))
            .catch(error => console.log(error))

    }

    return (
        <div className="App">
            <br />
            <br />
            {isLogin ? <h1>Please Login </h1> : <h1>Please Register </h1>}


            <br />
            <br />

            {isLogin ? <h1></h1> : <div className="mb-3">
                <label htmlFor="email" className="form-label">Username</label>
                <input type="email" className="form-control" id="email" placeholder="Please Enter Email"
                    value={email} onChange={e => setEmail(e.target.value)}
                />

            </div>}
            <div className="mb-3">
                <label htmlFor="username" className="form-label">Username</label>
                <input type="text" className="form-control" id="username" placeholder="Please Enter Username"
                    value={username} onChange={e => setUsername(e.target.value)}
                />

            </div>

            <div className="mb-3">
                <label htmlFor="password" className="form-label">Password</label>
                <input type="password" className="form-control" id="password" placeholder="Please Enter Password"
                    value={password} onChange={e => setPassword(e.target.value)}

                />

            </div>

            {isLogin ? <button onClick={loginBtn} className="btn btn-primary">Login</button>
                : <button onClick={RegisterBtn} className="btn btn-primary">Register</button>
            }


            <div className="mb-3">
                <br />
                {isLogin ? <h5>If You Don't Have Account, Please <button className="btn btn-primary" onClick={() => setLogin(false)} >Register</button>Here</h5>

                    : <h5>If You Have Account, Please <button className="btn btn-primary" onClick={() => setLogin(true)} >Login</button>Here</h5>
                }

            </div>
            <h1>{localStorage.getItem('auth_token')}</h1>
        </div>
    )
}

export default Login
