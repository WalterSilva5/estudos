import Header from "./index/Header";
import Gastos from "./index/Gastos";
class Index extends React.Component {
  render() {
    return (
      <div className="container col-12 d-flex">
        <div className="container col-8 mt-4">
          <Header />

          <Gastos />
        </div>
      </div>
    );
  }
}

export default Index;
