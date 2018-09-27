import React from 'react';
import { Row, Col, Container } from 'reactstrap';

const NavBar = (props) => {
    return (
      <div className="menu-wrapper">
        <Container>
         <nav> 
          <ul>
            <li ><a href="#">Home</a></li>
            <li ><a href="#">About Us</a></li>
            <li ><a href="#">Exemplos</a></li>
            <li ><a href="#">Contact</a></li>
          </ul>
        </nav>
        </Container>
      </div>
    ); 
}

export default NavBar;