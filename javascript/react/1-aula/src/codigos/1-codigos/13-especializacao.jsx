import ReactDom from "react-dom";


function Dialog(props) {
  return (
    <div>
      <h1 className="Dialog-title">
        {props.title}
      </h1>
      <p className="Dialog-message">
        {props.message}
      </p>
    </div>
  );
}

function App() {
  return (
    <Dialog
      title="Welcome"
      message="Thank you for visiting our spacecraft!" />
  );
}
ReactDom.render(<App />, document.getElementById("root"));