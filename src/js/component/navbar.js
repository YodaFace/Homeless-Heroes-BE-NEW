import React from "react";
import { Link } from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import NavDropdown from "react-bootstrap/NavDropdown";
import FormControl from "react-bootstrap/FormControl";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";

export const NavBar = () => {
	return (
		<Navbar bg="dark" expand="dark" variant="dark">
			<Navbar.Brand href="#home">HOMELESS AND HEROES</Navbar.Brand>
			<Button variant="warning">
				<i className="fas fa-user-circle fa-3x mr-auto" />
			</Button>
			<Button variant="warning" size="lg">
				DONATE
			</Button>
			<Navbar.Toggle aria-controls="basic-navbar-nav" />
			<Navbar.Collapse id="basic-navbar-nav">
				<Nav className="mr-auto">
					<NavDropdown title="Dropdown" id="basic-nav-dropdown">
						<NavDropdown.Item href="#home">HOME</NavDropdown.Item>
						<NavDropdown.Item href="#action/3.2">LOG IN</NavDropdown.Item>
						<NavDropdown.Item href="#action/3.3">HOW WE ARE</NavDropdown.Item>
						<NavDropdown.Item href="#action/3.4">HOW IT WORKS</NavDropdown.Item>
						<NavDropdown.Item href="#action/3.5">GET INVOLVED</NavDropdown.Item>
						<NavDropdown.Item href="#action/3.6">OUR PARTNERS</NavDropdown.Item>
						<NavDropdown.Divider />
						<NavDropdown.Item href="#action/3.7">
							<i className="fab fa-facebook fa-3x" />
							<i className="fab fa-twitter-square fa-3x" />
							<i className="fab fa-instagram fa-3x" />
						</NavDropdown.Item>
					</NavDropdown>
				</Nav>
			</Navbar.Collapse>
		</Navbar>
	);
};
