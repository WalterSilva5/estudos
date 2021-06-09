import ReactDom from "react-dom";

class Clock extends React.Component {
  
  clique(){
    alert("botão clicado");
  }
  
  render() {
    return (
      <div>
        <button onClick={this.clique}>TESTE</button>       
        <button onClick={(e) => this.deleteRow(id, e)}>Delete Row</button>
      </div>
    );
  }
}

ReactDom.render(<Clock />, document.getElementById("root"));
