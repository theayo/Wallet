import logo from './logo.svg';
import './App.css';
import {Button} from 'react-bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './Component/Header';  

import React, { Component }  from 'react';
function App() {
  {localStorage.setItem('InLogin', false)}
  return (
    <div>
      <Header></Header>
    </div>
  );
}

export default App;
