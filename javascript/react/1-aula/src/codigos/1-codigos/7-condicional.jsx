import ReactDom from "react-dom";

class App extends React.Component {
  logado = true;
  
  render() {
      if(this.logado){
        return <h1>esta logado</h1>
      }else{
        return <h1>não esta logado</h1>
      }
    }
}

ReactDom.render(<App />, document.getElementById("root"));
