import React, { Component, useEffect, useState } from 'react'
import APIService from '../Component/APIService'
import Login from '../Pages/Login'


export default function Home() {
    const [username, setUsername] = useState('')
    const [walletValue, setWalletValue] = useState('')


    useEffect(() => {
        fetch('http://127.0.0.1:8000/api/v1/wallet/get_user_wallet/', {
            'method': 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${localStorage.getItem("token")}`
            }
        })
            .then(resp => resp.json())
            .then(resp => setWalletValue(resp.usd))
            .catch(error => console.log(error))

    }, [])

    return (
        <div>
            {Login.token}
            {walletValue}
        </div>
    )
}
