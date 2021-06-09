class Componente extends React.Component {
  state = {
    nome: "teste",
  };
  mudarNome = () => {
    console.log("clicado");
    this.setState({
      nome: "filterText",
    });
  };

  render() {
    return (
      <div>
        <h1>{this.state.nome}</h1>
        <button onClick={this.mudarNome}>mudar nome</button>
      </div>
    );
  }
}

class App extends React.Component {
  render() {
    return <Componente nome="walter" />;
  }
}

export default App;
