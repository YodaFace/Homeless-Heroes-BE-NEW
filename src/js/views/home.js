import React from "react";
import Form from "react-bootstrap/Form";
import FormControl from "react-bootstrap/FormControl";
import rigoImage from "../../img/rigo-baby.jpg";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import "../../styles/home.scss";

export const Home = () => (
	<div className="text-center">
		<Container className="email-holder">
			<input className="form-control" placeholder="Who are you looking for ?" />
			<button type="submit" className="btn">
				{" "}
				<i className="fas fa-search" />{" "}
			</button>
			<div />
		</Container>
		<div className="text-center mt-5">
			<p>
				<img src="https://news.berkeley.edu/wp-content/uploads/2018/10/ronBIDstudy750.png" />
			</p>
			<a href="#" className="btn btn-success">
				If you see this green button, bootstrap is working
			</a>
		</div>
	</div>
);
