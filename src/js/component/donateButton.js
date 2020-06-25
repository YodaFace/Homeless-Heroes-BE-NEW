import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import ModalDialog from "react-bootstrap/ModalDialog";
import ModalHeader from "react-bootstrap/ModalHeader";
import ModalTitle from "react-bootstrap/ModalTitle";
import ModalBody from "react-bootstrap/ModalBody";
import ModalFooter from "react-bootstrap/ModalFooter";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import FormControl from "react-bootstrap/FormControl";

export const DonateButton = () => {
	const [show, setShow] = useState(false);

	const handleClose = () => setShow(false);
	const handleShow = () => setShow(true);
	const [validated, setValidated] = useState(false);

	const handleSubmit = event => {
		const form = event.currentTarget;
		if (form.checkValidity() === false) {
			event.preventDefault();
			event.stopPropagation();
		}

		setValidated(true);
	};
	return (
		<>
			<Button className="donatebtn" onClick={handleShow}>
				DONATE
			</Button>

			<Modal show={show} onHide={handleClose} animation={false}>
				<Modal.Header closeButton>
					<Modal.Title>QUICK DONATE</Modal.Title>
				</Modal.Header>
				<Modal.Body>
					<Form noValidate validated={validated} onSubmit={handleSubmit}>
						<Form.Group controlId="validationCustom01">
							<Form.Label>Name</Form.Label>
							<Form.Control required type="text" defaultValue="" />
							<Form.Control.Feedback>Looks good!</Form.Control.Feedback>
						</Form.Group>
						<Form.Group controlId="validationCustom02">
							<Form.Label>ZIP CODE</Form.Label>
							<Form.Control type="text" placeholder="5 digit" required />
							<Form.Control.Feedback type="invalid">Please provide a valid zip.</Form.Control.Feedback>
						</Form.Group>
						<Form.Group controlId="validationDonationAmount">
							<Form.Label>DONATE AMOUNT</Form.Label>
							<InputGroup>
								<InputGroup.Prepend>
									<InputGroup.Text id="inputGroupPrepend">$</InputGroup.Text>
								</InputGroup.Prepend>
								<Form.Control
									type="text"
									placeholder="ENTER A DOLLAR AMOUNT"
									aria-describedby="inputGroupPrepend"
									required
								/>
								<Form.Control.Feedback type="invalid">Please enter an amount.</Form.Control.Feedback>
							</InputGroup>
						</Form.Group>
						<Form.Group>
							<Form.Check
								required
								label="Agree to terms and conditions"
								feedback="You must agree before submitting."
							/>
						</Form.Group>
					</Form>
				</Modal.Body>
				<Modal.Footer>
					<Button type="submit" variant="primary" onClick={handleClose}>
						DONATE NOW
					</Button>
				</Modal.Footer>
			</Modal>
		</>
	);
};
