import React from "react";
import { Link } from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import NavDropdown from "react-bootstrap/NavDropdown";
import FormControl from "react-bootstrap/FormControl";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import ListGroup from "react-bootstrap/ListGroup";
import ButtonGroup from "react-bootstrap/ButtonGroup";

export const NavBar = () => {
	return (
		<Navbar bg="dark" expand="dark" variant="dark">
			<Navbar.Toggle aria-controls="basic-navbar-nav" />
			<Navbar.Brand href="#home" className="mr-auto p-3">
				HOMELESS AND HEROES
			</Navbar.Brand>
			<Link to="/demo">
				<Button variant="light " className="d-flex justify-content-end mr-3">
					<i className="fas fa-user fa-3x" />
				</Button>
			</Link>
			<Button bg="warning" variant="warning" size="xxl" type="text-white" className="p-3">
				DONATE
			</Button>
			<Navbar.Collapse id="basic-navbar-nav">
				<Nav className="mr-auto">
					<Link to="/">
						<ListGroup.Item href="#home">HOME</ListGroup.Item>
					</Link>
					<ListGroup.Item href="#action/3.1">LOG IN</ListGroup.Item>
					<ListGroup.Item href="#action/3.2">HOW WE ARE</ListGroup.Item>
					<ListGroup.Item href="#action/3.3">HOW IT WORKS</ListGroup.Item>
					<ListGroup.Item href="#action/3.4">GET INVOLVED</ListGroup.Item>
					<ListGroup.Item href="#action/3.5">OUR PARTNERS</ListGroup.Item>
					<NavDropdown.Divider />
					<ListGroup.Item href="#action/3.6">
						<i className="fab fa-facebook fa-3x p-3" />
						<i className="fab fa-twitter-square fa-3x p-3" />
						<i className="fab fa-instagram fa-3x p-3" />
					</ListGroup.Item>
				</Nav>
			</Navbar.Collapse>
		</Navbar>
	);
};
