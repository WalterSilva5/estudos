import ReactDom from "react-dom";
import Index from './components/Index.jsx'
import './assets/scss/styles.scss'
import 'bootstrap/dist/css/bootstrap.css';


class App extends React.Component {

  render(){
    return(
      <Index/>
    )
  }
}

ReactDom.render(
  <App/>,
  document.getElementById('root')
);