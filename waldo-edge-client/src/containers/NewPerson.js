import uuid from "uuid";
import React, { Component } from "react";
import { FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import LoaderButton from "../components/LoaderButton";
import config from "../config";
import "./NewPerson.css";
import { API } from "aws-amplify";
import { s3Upload } from "../libs/awsLib";

export default class NewNote extends Component {
  constructor(props) {
    super(props);

    this.file = null;

    this.state = {
      isLoading: null,
      name: "",
      phone: "",
      notes: ""
    };
  }

  validateForm() {
    return this.state.name.length > 0;
  }

  handleChange = event => {
    this.setState({
      [event.target.id]: event.target.value
    });
  };

  handleFileChange = event => {
    this.file = event.target.files[0];
  };

  handleSubmit = async event => {
    event.preventDefault();

    if (this.file && this.file.size > config.MAX_ATTACHMENT_SIZE) {
      alert(
        `Please pick a file smaller than ${config.MAX_ATTACHMENT_SIZE /
          1000000} MB.`
      );
      return;
    }

    this.setState({ isLoading: true });

    try {
      const personID = uuid.v1();
      const attachment = this.file
        ? await s3Upload(this.file, personID, this.state.name, this.state.phone)
        : null;
      await this.upload({
        attachment,
        ID: personID,
        name: this.state.name,
        phone: this.state.phone,
        notes: this.state.notes
      });
      this.props.history.push("/");
    } catch (e) {
      alert(e);
      this.setState({ isLoading: false });
    }
  };

  upload(person) {
    return API.post("waldo-edge", "/upload", {
      body: person
    });
  }

  render() {
    return (
      <div className="NewPerson">
        <form onSubmit={this.handleSubmit}>
          <FormGroup controlId="name">
            <ControlLabel>Name</ControlLabel>
            <FormControl
              type="text"
              value={this.state.name}
              placeholder="Richard Nixon"
              onChange={this.handleChange}
            />
          </FormGroup>
          <FormGroup controlId="phone">
            <ControlLabel>Contact Phone Number</ControlLabel>
            <FormControl
              type="text"
              value={this.state.phone}
              placeholder="XXX-XXX-XXXX"
              onChange={this.handleChange}
            />
          </FormGroup>
          <FormGroup controlId="notes">
            <ControlLabel>Notes</ControlLabel>
            <FormControl
              onChange={this.handleChange}
              value={this.state.notes}
              placeholder="Last seen at corner of 12th and madison . . ."
              componentClass="textarea"
            />
          </FormGroup>
          <FormGroup controlId="file">
            <ControlLabel>Attach photos below</ControlLabel>
            <FormControl onChange={this.handleFileChange} type="file" />
          </FormGroup>
          <LoaderButton
            block
            bsStyle="primary"
            bsSize="large"
            disabled={!this.validateForm()}
            type="submit"
            isLoading={this.state.isLoading}
            text="Create"
            loadingText="Creating…"
          />
        </form>
      </div>
    );
  }
}
