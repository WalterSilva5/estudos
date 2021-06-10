import Mes from "./Mes";
class gastos extends React.Component {
  gastos = [];
  render() {
    let linhas = this.gastos.map((valor) => {
      return <Mes valor={valor} key={valor}></Mes>;
    });
    return <div className="rounded py-4 bg-warning d-flex">{linhas}</div>;
  }
}

export default gastos;
