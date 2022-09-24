import React, { Component, useState, useEffect } from 'react'

function Withdraw() {
  const [wallet, setWallet] = useState(0)
  const [sendWallet, setSendWallet] = useState('')
  const [walletId, setWalletId] = useState(0)

  useEffect( ()=> {
    fetch('http://127.0.0.1:8000/api/v1/wallet/get_user_wallet/', {
      'method': 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${localStorage.getItem('auth_token')}`
      }
    })
      .then(resp => resp.json())
      .then(resp => setWallet(resp.usd))
      .catch(error => console.log(error))
  },[])

  const Send = (body) => {
    fetch('http://127.0.0.1:8000/api/v1/wallet/deposit_funds/', {
      'method': 'PUT',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Token ${localStorage.getItem('auth_token')}`
      },
      body: JSON.stringify(body)
    })
      .then(resp => resp.json(), resp => console.log(resp.JSON()))
      .catch(error => console.log(error))

  } 
  return (
    <div>
      {!localStorage.getItem("InLogin") ? <h1>зарегстрируйся петушок</h1> :

        <div className="mb-3">
          <div>
            <label htmlFor="wallet" className="form-label">{wallet}</label>
          </div>
          <label htmlFor="sendWallet" className="form-label">Your wallet</label>
          <input type="text" className="form-control" id="sendWallet" placeholder="Please Enter withdraw from your wallet"
            value={sendWallet} onChange={e => setSendWallet(e.target.value)}
          />
          <label htmlFor="walletId" className="form-label">Your id </label>
          <input type="text" className="form-control" id="walletId" placeholder="Please Enter Id your wallet"
            value={walletId} onChange={e => setWalletId(e.target.value)}
          />
          <button onClick={Send({ sendWallet, walletId })} className="btn btn-primary">Send</button>
        </div>}

    </div>
  )
}

export default Withdraw