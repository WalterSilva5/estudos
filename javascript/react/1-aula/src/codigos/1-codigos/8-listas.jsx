import ReactDom from "react-dom";

class App extends React.Component {
  lista = ["a", "b", "c"];
  render() {
    let linhas = this.lista.map((letra) => {
      return <li key={letra}>{letra}</li>;
    });
    console.log(linhas)
    return <ul>{linhas}</ul>
  }
}

ReactDom.render(<App />, document.getElementById("root"));
