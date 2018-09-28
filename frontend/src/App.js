import React, { Component } from 'react';
import './App.css';
import { Row, Col, Container } from 'reactstrap';
import NavBar from "./components/NavBar"
import Home from "./components/Home"
import Description from "./components/Description"
import Footer from "./components/Footer"
import Examples from "./components/Examples"
import ReactDOM from 'react-dom';

class App extends Component {
  constructor(props) {
    super(props);    
    this.examples_ref = React.createRef();
    this.footer_ref = React.createRef();
    this.description_ref = React.createRef();
    this.focusFooter = this.focusFooter.bind(this);
    this.focusExamples = this.focusExamples.bind(this);
    this.focusDescription = this.focusDescription.bind(this);
  }

  focusExamples() {
    const domNode = ReactDOM.findDOMNode(this.examples_ref.current)    
    domNode.scrollIntoView()
  }

  focusFooter() {
    const domNode = ReactDOM.findDOMNode(this.footer_ref.current)    
    domNode.scrollIntoView()
  }

  focusDescription() {
    const domNode = ReactDOM.findDOMNode(this.description_ref.current)    
    domNode.scrollIntoView()
  }

  render() {
    return (
      <div className="App">
        <Row >
            <Col>            
              <Row className="menu">
                <Col >
                  <NavBar focusExamples={this.focusExamples} focusFooter={this.focusFooter} focusDescription={this.focusDescription} />
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
                    <Description  refsection={this.description_ref}/>
                    <hr/>
                    <Examples refsection={this.examples_ref} />
                    <hr />                    
                  </Container>
                </Col>
              </Row>
              <Row className="footer-body">
                <Col>
                  <Footer refsection={this.footer_ref} />    
                </Col>
              </Row>              
            </Col>
        </Row>
      </div>
    );
  }
}

export default App;
