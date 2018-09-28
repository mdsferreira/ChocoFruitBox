import React from 'react';
import { Button, Row, Col, Container, Form, FormGroup, Label, Input } from 'reactstrap';

const Footer = (props) => {
    return (
        <section id="footer" ref={props.refsection}>
        <Container>
            <Row>
                <Col >
                    <Row>
                        <Col>
                            <h2 className="section-title">Contact Us</h2>
                        </Col>
                        <Col>
                            <Form>
                            <Row>                            
                                <Col>                                
                                    <FormGroup>
                                    <Label for="contactEmail">Email</Label>
                                    <Input type="email" name="email" id="contactEmail" placeholder="your email" />
                                    </FormGroup>                                    
                                </Col>
                            </Row>
                            <Row>                            
                                <Col>                                
                                    <FormGroup>
                                    <Label for="contactSubject">Subject</Label>
                                    <Input type="text" name="subject" id="contactSubject" placeholder="subject" />
                                    </FormGroup>                                    
                                </Col>
                            </Row>
                            <Row>                            
                                <Col>                                
                                    <FormGroup>
                                    <Label for="contactText">Menssage</Label>
                                    <Input type="textarea" name="contact" id="contactText" placeholder="type your menssage here..." />
                                    </FormGroup>                                    
                                </Col>
                            </Row>
                                <Row>                            
                                    <Col>                                
                                        <Button color="secondary">Send</Button>
                                    </Col>
                                </Row>
                            </Form>
                        </Col>
                    </Row>
                </Col>
            </Row>
        </Container>
        </section>
    ); 
}

export default Footer;