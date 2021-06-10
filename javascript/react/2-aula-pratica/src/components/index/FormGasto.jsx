class FormGasto extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      descricao: "",
      valor: "",
      data: "",
    };
  }

  inputDescricao = (e) => {
    this.setState({ descricao: e.target.value });
  };

  inputValor = (e) => {
    this.setState({ valor: e.target.value });
  };

  inputData = (e) => {
    this.setState({
      data: new Date(e.target.value).toLocaleDateString(),
    });
  };

  salvarForm = (e) => {
    console.log(this.props.valorespai);
    this.props.valorespai.push([
      this.state.descricao,
      this.state.valor,
      this.state.data,
    ]);
    console.log(this.props.valorespai);
  };

  render() {
    return (
      <div className=" justify-content-center d-flex">
        <div className="form row py-5 container border border-secondary rounded">
          <label htmlFor="descricao">Descricao</label>
          <input
            type="text"
            id="descricao"
            className="form-control"
            onChange={this.inputDescricao}
            value={this.state.descricao}
          />
          <label htmlFor="valor">Valor</label>
          <input
            type="text"
            id="valor"
            className="form-control"
            onChange={this.inputValor}
            value={this.state.valor}
          />
          <label htmlFor="dataEntrada">Data</label>
          <input
            type="date"
            id="dataEntrada"
            className="form-control"
            onChange={this.inputData}
            value={this.state.data}
          />
          <div>
            <button
              className="btn btn-primary btn-lg float-end mt-3"
              onClick={this.salvarForm}
            >
              ADICIONAR
            </button>
          </div>
        </div>
      </div>
    );
  }
}

export default FormGasto;
