import React, { useState } from "react";
import { Link } from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import NavDropdown from "react-bootstrap/NavDropdown";
import FormControl from "react-bootstrap/FormControl";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import ListGroup from "react-bootstrap/ListGroup";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import { DonateButton } from "./donateButton";

export const NavBar = () => {
	const [expanded, setExpanded] = useState(false);
	return (
		<Navbar className="navbar" expand="dark" expanded={expanded} variant="dark">
			<Navbar.Toggle
				className="hamburger"
				aria-controls="basic-navbar-nav"
				onClick={() => setExpanded(expanded ? false : "expanded")}
			/>
			<Navbar.Brand href="#home" className="mr-auto p-3" onClick={() => setExpanded(false)}>
				<Link to="/" h1>
					HOMELESS AND HEROES
				</Link>
			</Navbar.Brand>
			<Link to="/demo">
				<Button variant="dark" className="d-flex justify-content-end mr-3" onClick={() => setExpanded(false)}>
					<i className="far fa-user fa-3x" />
				</Button>
			</Link>
			<DonateButton className="donatebtn" />
			<Navbar.Collapse id="basic-navbar-nav">
				<Nav className="mr-auto">
					<Link to="/">
						<ListGroup.Item href="#home" onClick={() => setExpanded(false)}>
							HOME
						</ListGroup.Item>
					</Link>
					<Link to="/login">
						<ListGroup.Item href="#action/3.1" onClick={() => setExpanded(false)}>
							LOG IN / REGISTER
						</ListGroup.Item>
					</Link>
					<ListGroup.Item href="#action/3.2" onClick={() => setExpanded(false)}>
						HOW WE ARE
					</ListGroup.Item>
					<ListGroup.Item href="#action/3.3" onClick={() => setExpanded(false)}>
						HOW IT WORKS
					</ListGroup.Item>
					<ListGroup.Item href="#action/3.4" onClick={() => setExpanded(false)}>
						GET INVOLVED
					</ListGroup.Item>
					<ListGroup.Item href="#action/3.5" onClick={() => setExpanded(false)}>
						OUR PARTNERS
					</ListGroup.Item>
					<NavDropdown.Divider />
					<ListGroup.Item>
						<a href="https://www.facebook.com/">
							<i className="fab fa-facebook fa-3x" />
						</a>
						<a href="https://www.twitter.com/">
							<i className="fab fa-twitter-square fa-3x p-3" />
						</a>
						<a href="https://www.instagram.com/">
							<i className="fab fa-instagram fa-3x p-3" />
						</a>
					</ListGroup.Item>
				</Nav>
			</Navbar.Collapse>
		</Navbar>
	);
};
