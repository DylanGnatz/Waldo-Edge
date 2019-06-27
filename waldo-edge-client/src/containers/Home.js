import React, { Component } from "react";
import "./Home.css";

export default class Home extends Component {
  render() {
    return (
      <div className="Home">
        <div className="lander">
          <h1>WaldoEdge</h1>
          <p>An edge computing prototype for finding missing persons</p>
        </div>
      </div>
    );
  }
}
