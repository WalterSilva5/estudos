import React from "react";

class Header extends React.Component {
  
  mudarPagina(pagina){
    this.props.mudarPagina(pagina)
  }

  render() {
    return (
      <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
        <a className="navbar-brand" href="#">
          Navbar
        </a>
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <button className="btn btn-primary" onClick={(e) => this.mudarPagina('Pagina1')}>PAGINA1</button>
          <button className="btn btn-primary mx-2" onClick={(e) => this.mudarPagina('Pagina2')}>PAGINA2</button>
        </div>
      </nav>
    );
  }
}

export default Header;
