import logo from './logo.svg';
import './App.css';
import CardGen from './CardGen.js';
function App() {
  return (
    <div className="App">
      <div className="App-header-bar-container">
        <div className="App-header-bar">
          <h2>Card Generator</h2>
        </div>
      </div>
      <div className="App-body">
        <div className="App-body-content">
          <p>Enter your contact information below and click "Generate" to download a vCard.</p>
          <CardGen />
        </div>
      </div>
    </div>
  );
}

export default App;