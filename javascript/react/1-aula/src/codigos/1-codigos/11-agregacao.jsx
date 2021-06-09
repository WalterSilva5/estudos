import ReactDom from "react-dom";

function JanelaFilha(props) {
  return (
    <div>
      {props.children}
    </div>
  );
}

function App() {
  return (
    <JanelaFilha>
      <h1 className="Dialog-title">
        Welcome
      </h1>
      <p className="Dialog-message">
        Thank you for visiting our spacecraft!
      </p>
    </JanelaFilha>
  );
}

ReactDom.render(<App />, document.getElementById("root"));
