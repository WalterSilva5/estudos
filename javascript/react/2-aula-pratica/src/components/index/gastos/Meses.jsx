import Mes from "./Mes";
class Meses extends React.Component {
  meses = [15, 20, 25, 30, 35];
  render() {
    let linhas = this.meses.map((valor)=>{return <Mes valor={valor} key={valor}></Mes>})
    return (
      <div className="rounded py-4 bg-warning d-flex">
        {linhas}
      </div>
    );
  }
}

export default Meses;
