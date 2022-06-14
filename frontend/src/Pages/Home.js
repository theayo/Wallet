import React, { Component, useEffect, useState } from 'react'
import APIService from '../Component/APIService'
import Login from '../Pages/Login'


export default function Home() {
    const [username, setUsername] = useState('')
    const [walletValue, setWalletValue] = useState('')
    const [email, setEmail] = useState('')

    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/v1/user/get_user/', {
            'method': 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
            }
        })
            .then(resp => resp.json())
            .then(resp => setUsername(resp.username),
            resp => setEmail(resp.email))
            .catch(error => console.log(error))

    fetch('http://127.0.0.1:8000/api/v1/wallet/get_user_wallet/', {
            'method': 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem('auth_token')}`
            }
        })
            .then(resp => resp.json())
            .then(resp => setWalletValue(resp.usd))
            .catch(error => console.log(error))

    }, [])

    return (
        <div>
            {!localStorage.getItem("InLogin") ? <h1>зарегстрируйся петушок</h1> :
                <div className="mb-3">
                    <div>
                        <label className="form-label">Привет, {username} {email}</label>
                    </div>
                    <label className="label">Вы сегодня такой богатый!!!!</label>
                    <div>
                        <label className="form-label">Your wallet</label>
                    </div>
                    <label className="label">{walletValue}</label>

                </div>}
        </div>
    )
}
