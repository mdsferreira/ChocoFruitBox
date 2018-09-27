import React, { Component } from 'react';
import './App.css';
import { Row, Col, Container } from 'reactstrap';
import NavBar from "./components/NavBar"
import Home from "./components/Home"
import Description from "./components/Description"
import Footer from "./components/Footer"
import Examples from "./components/Examples"

class App extends Component {
  render() {
    return (
      <div className="App">
        <Row >
            <Col>            
              <Row className="menu">
                <Col >
                  <NavBar />
                </Col>
              </Row>
              <Row className="home-body">
                <Col>
                  <Home />
                </Col>
              </Row>
              <Row>
                <Col className="body-site">
                  <Container>                    
                    <Description />
                    <hr/>
                    <Examples />
                    <hr />
                    
                  </Container>
                </Col>
              </Row>
              <Row className="footer-body">
                <Col>
                  <Footer />    
                </Col>
              </Row>              
            </Col>
        </Row>
      </div>
    );
  }
}

export default App;
