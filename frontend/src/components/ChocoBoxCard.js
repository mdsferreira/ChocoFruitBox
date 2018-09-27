import React from 'react';
import { Container, Card, Row, Col } from 'reactstrap';

const ChocoBoxCard = (props) => {
    return (        
        <Row>
            <Col md="4">
                <img  src={props.img} alt="project-img"/>
            </Col>
            <Col md="8">
                teste  
            </Col>
        </Row>           
    ); 
}

export default ChocoBoxCard;

