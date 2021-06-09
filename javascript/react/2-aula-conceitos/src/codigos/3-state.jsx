import ReactDom from "react-dom";
import React, { Component } from "react";
import logo from "./favicon.svg";

//componente
function Relogio(props) {
  return (
    <div>
      <h2>Agora são: {props.hora.toLocaleTimeString()}</h2>
    </div>
  );
}

class App extends Component {
  render() {
    return <Relogio hora={new Date()}/>;
  }
}

setInterval(() => {
  ReactDom.render(<App />, document.getElementById("root"));
}, 1000);
