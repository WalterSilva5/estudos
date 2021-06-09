import React from "react";
import Header from "./index/Header";
import Pagina1 from "./Pagina1";
import Pagina2 from "./Pagina2";
class Index extends React.Component {
  state = {
    PaginaAtual: 'Pagina1'};

  mudarPagina = (value) => {
    this.setState({ PaginaAtual: value }); 
  };


  render() {
    let Pagina = ''
    if(this.state.PaginaAtual == 'Pagina1'){
      Pagina = Pagina1
    }
    else{
      Pagina = Pagina2
    }
    return (
      <div>
        <Header
          mudarPagina={this.mudarPagina}
        />

        <Pagina/>
      </div>
    );
  }
}

export default Index;
