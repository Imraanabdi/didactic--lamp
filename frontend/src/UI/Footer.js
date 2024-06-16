import React from "react";
import { Container, Row, Col } from "react-bootstrap";

const stickyFooterStyle = {
    backgroundColor: '#2b3035',
    fontSize: "13px",
    color: "white",
    borderTop: "1px solid #E7E7E7",
    textAlign: "center",
    padding: "20px",
    position: "fixed",
    left: "0",
    bottom: "0",
    height: "30px",
    width: "100%"
  };

function Footer() {
  return (
    <>
      <Container>
        <Row>
          <Col style={stickyFooterStyle} sm={12}>
            &copy; Copyright 2024 - imran abdisalan
          </Col>
        </Row>
      </Container>
    </>
  );
}

export default Footer;
