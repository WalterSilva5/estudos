import Header from "./index/Header";
import Gastos from "./index/Gastos";
import FormGasto from "./index/FormGasto";
class Index extends React.Component {
  state = {
    valores: [],
  };

  render() {
    return (
      <div className="container col-12 d-flex">
        <div className="container col-8 mt-4">
          <Header />
          <FormGasto valorespai={this.state.valores} />
          <Gastos />
        </div>
      </div>
    );
  }
}

export default Index;
