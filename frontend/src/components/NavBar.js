import React from 'react';
import { Container } from 'reactstrap';

const NavBar = (props) => {
    return (
      <div className="menu-wrapper">
        <Container>
         <nav> 
          <ul>
            <li ><a href="/#">Home</a></li>
            <li onClick={props.focusDescription}><a>About Us</a></li>
            <li onClick={props.focusExamples}><a>Exemplos</a></li>
            <li onClick={props.focusFooter}><a>Contact</a></li>
          </ul>
        </nav>
        </Container>
      </div>
    ); 
}

export default NavBar;