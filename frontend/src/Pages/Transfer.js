import React, { Component, useState } from 'react'

export default function Transfer() {


    const [walletFrom, setWalletFrom] = useState('');
    const [walletWhere, setWalletWhere] = useState('');
    return (
        <div>
            {!localStorage.getItem("InLogin") ? <h1>зарегстрируйся петушок</h1> :
                <div className="mb-3">
                    <label htmlFor="walletFrom" className="form-label">Your walletFrom</label>
                    <input type="text" className="form-control" id="walletFrom" placeholder="Please Enter Id your walletFrom"
                        value={walletFrom} onChange={e => setWalletFrom(e.target.value)}
                    />
                    {walletFrom}
                    <label htmlFor="walletWhere" className="form-label">Your Wallet</label>
                    <input type="text" className="form-control" id="walletWhere" placeholder="Please Enter Id another Wallet"
                        value={walletWhere} onChange={e => setWalletWhere(e.target.value)}
                    />
                </div>}
        </div>
    )
}
