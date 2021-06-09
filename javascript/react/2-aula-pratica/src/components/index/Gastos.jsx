import Filtro from "./gastos/Filtro";
import Meses from "./gastos/Meses";
class Gastos extends React.Component {
  render() {
    return (
      <div>
        <Filtro />
        <Meses />
        <div></div>
      </div>
    );
  }
}

export default Gastos;
