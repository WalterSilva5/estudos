import logo from "./favicon.svg";

class App extends React.Component {
  render() {
    return (
      <div className="App">
        <h1> {this.props.nome}</h1>
        <h1> {logo}</h1>
      </div>
    );
  }
}

//<App  nome="walter" />,
export default App;

