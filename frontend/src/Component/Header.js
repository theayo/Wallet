import React, { Component } from 'react'
import { Container, Form, Nav, Navbar, FormControl, Button } from 'react-bootstrap'
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom'
import logo from './logo192.png'
import Home from '../Pages/Home'
import Transfer from '../Pages/Transfer'
import Withdraw from '../Pages/Withdraw'
import Login from '../Pages/Login'


export default class Header extends Component {
    render() {
        return (
            <>
                <Navbar fixed="top" sticky='top' collapseOnSelect expand="sm" bg="dark" variant="dark">
                    <Container>
                        <Navbar.Brand href="/">
                            <img
                                src={logo}
                                height="70"
                                width="70"
                                className='d-inline-block align-top'
                                alt="logo"
                            />
                        </Navbar.Brand>
                        <Navbar.Toggle aria-controls="responsive-navbar-nar" />
                        <Navbar.Collapse id="responsive-navbar-nav">
                            <Nav className="me-auto">
                                <Nav.Link href="/"> <font color="#fa8e47">Мой кошелек</font></Nav.Link>
                                <Nav.Link href="/transfer">Перевести</Nav.Link>
                                <Nav.Link href="/withdraw">Снять</Nav.Link>
                                <Nav.Link href="/withdraw">Пополнить баланс</Nav.Link>
                                <Nav.Link href="/login">Зайти</Nav.Link>
                            </Nav>
                            <Form className="form-inline"> {/*я ебу почему inline не работает*/}
                                <FormControl
                                    type="text"
                                    placeholder="Search"
                                    className="me-sm-2"
                                />
                                <Button variant="outline-info">Search</Button>
                            </Form>
                        </Navbar.Collapse>
                    </Container>
                </Navbar>

                <Router>
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/transfer" element={<Transfer />} />
                        <Route path="/withdraw" element={<Withdraw />} />
                        <Route path="/login" element={<Login/>} />
                    </Routes>
                </Router>
            </>
        )
    }
}
