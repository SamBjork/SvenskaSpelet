import logo from './ssr.png';
import './App.css';




function App() {

  function sayHello(){
    alert("Hello! Soon you can log in here")
  }
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} id="App-logo" alt="logo" />
        <br/>
        Välkommen till
          <br/>
          "Svenska Spelet"
        <button onClick={sayHello}>
          Logga in
        </button>
        <button onClick={sayHello}>
          Registera dig
        </button>
        <button onClick={sayHello}>
          Se topplistan
        </button>
      </header>
    </div>
  );
}

export default App;
