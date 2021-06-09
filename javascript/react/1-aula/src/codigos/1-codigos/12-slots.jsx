import ReactDom from "react-dom";

function SplitPane(props) {
  return (
    <div>
      <div>{props.left}</div>
      <div>{props.right}</div>
    </div>
  );
}

function App() {
  return <SplitPane left={<Contacts />} right={<Chat />} />;
}

ReactDom.render(<App />, document.getElementById("root"));
