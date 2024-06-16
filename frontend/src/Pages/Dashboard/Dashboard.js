import React from "react";
import { Container, Row, Col } from "react-bootstrap";
import "./Dashboard.css";

function Dashboard() {
  return (
    <div className="home">
      <div className="titleblock">
        <h3>Dashboard</h3>
      </div>
      <Container className="content">
        <Row>
          <Col>
            <p>
              Dashboard with cards and more
            </p>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Dashboard;
