class Header extends React.Component {
  
  mudarPagina(pagina){
    this.props.mudarPagina(pagina)
  }

  render() {
    return (
      <nav className="rounded navbar navbar-expand-lg navbar-dark bg-dark">
        <div className="container d-flex justify-content-center">
          <button className="btn btn-primary btn-lg"><b>ADICIONAR NOVO GASTO</b></button>
        </div>
      </nav>
    );
  }
}

export default Header;
