import React, { Component } from "react";
import ReactDom from 'react-dom'
import logo from "./favicon.svg";

let nome = "walter silva"

class App extends Component {
  render() {
    return (
      <div className="App">
        <h1> {nome}</h1>
        <img src="{logo}"/>
      </div>
    );
  }
}

export default App;

ReactDom.render(<App />, document.getElementById("root"));