class Filtro extends React.Component {
  render() {
    return (
      <div className="bg-secondary rounded py-4 container d-flex justify-content-between">
        <span>FILTRAR PRO ANO</span>

        <div className="form-group">
          <select className="form-select" name="ano" id="ano">
            <option value="2019">2019</option>
            <option value="2020">2020</option>
            <option value="2021">2021</option>
          </select>
        </div>
      </div>
    );
  }
}

export default Filtro;
