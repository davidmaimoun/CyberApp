import React from 'react';
import MyButton from './all/Button';
import logo from '../assets/logo1.webp'

const Header: React.FC = () => {
  return (
    <header className="header">
      <div className="header-logo">
        <img src={logo} alt="Logo" className="header-logo-image" />
      </div>

      <nav className="nav">
        <a href="/scan" className="nav-link">Scan</a>
        <a href="/help" className="nav-link">Help</a>
      </nav>

      <div className="header-login">
        <MyButton 
            label={'Login'} 
            onClick={function (): void {
                  throw new Error('Function not implemented.');
              }}/>
      </div>
    </header>
  );
};

export default Header;
