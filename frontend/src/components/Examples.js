import React from 'react';
import { Row, Col, Nav, NavItem, NavLink, TabContent, TabPane } from 'reactstrap';
import ChocoBoxCard from "./ChocoBoxCard"
import classnames from 'classnames';

class Examples extends React.Component {
        constructor(props) {
          super(props);
      
          this.toggle = this.toggle.bind(this);
          this.state = {
            activeTab: '1'
          };
        }
        toggle(tab) {
            if (this.state.activeTab !== tab) {
              this.setState({
                activeTab: tab
              });
            }
          }
    render() {
        return (
            <section id="examples" > 
            <Row>
            <Col md="10">
                <h2 className="section-title">Examples</h2>
                <div>
                    <Nav tabs>
                    <NavItem>
                        <NavLink 
                        className={classnames({ active: this.state.activeTab === '1' })}
                        onClick={() => { this.toggle('1'); }}
                        >
                        ChocoFruit 1
                        </NavLink>
                    </NavItem>
                    <NavItem>
                        <NavLink
                        className={classnames({ active: this.state.activeTab === '2' })}
                        onClick={() => { this.toggle('2'); }}
                        >
                        ChocoFruit 2
                        </NavLink>
                    </NavItem>
                    </Nav>
                    <TabContent activeTab={this.state.activeTab}>
                    <TabPane tabId="1"> 
                    <ChocoBoxCard img="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSwldb2lIPyGFRhScP4S2hV9azsdIP6PKkVyPvH0bU69GgIZiZrQ" />                       
                    </TabPane>   
                    <TabPane tabId="2">
                    <ChocoBoxCard img="https://cdn.shopify.com/s/files/1/0804/5989/products/K-NewCatalog-GiftBox6_1280x1280.png?v=1489262849" />                       
                    </TabPane>                 
                    </TabContent>
                </div>
                        
            </Col>
            </Row>
        </section>
        ); 
    }
}

export default Examples;