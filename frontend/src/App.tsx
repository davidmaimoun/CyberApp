import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { ToastContainer } from 'react-toastify';
import Home from "./components/Home";
import Scan from "./components/Scan";
import Header from "./components/Header";

const App: React.FC = () => {

  return (
    <div className="app-container">
      <ToastContainer aria-label={undefined}/>
      <Header/>

      <div className="main-content">
        <aside className="left-side">
        </aside>
        
        <main className="main">
          <Router>
            <Routes>
            <Route path="/" element={<Scan />} />
            <Route path="/home" element={<Home />} />
            </Routes>
        </Router>
        </main>
        
        <aside className="right-side">
        </aside>
      </div>

      {/* <footer className="footer">
        <p>Footer Content</p>
      </footer> */}
  </div>

  );
};

export default App;
