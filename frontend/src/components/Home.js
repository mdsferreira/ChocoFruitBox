import React from 'react';
import { Row, Col, Container} from 'reactstrap';

const Home = (props) => {
    return (
      <Container>
        <Row>
          <Col className="home-label"> 
            <p className="home-brand">ChocoFruit Box</p>
            <p className="home-slogan">special chocolates just for you</p> 
            <p class="home-social">
              <a href="" target="_blank"><i class="fa fa-github"></i></a>
              <a href="" target="_blank"><i class="fa fa-linkedin-square"></i></a>
              <a href="" target="_blank"><i class="fa fa-facebook-square"></i></a>
            </p>           
          </Col>
        </Row>
      </Container>

    ); 
}

export default Home;