import "./Timesheets.css";
import React, { useState, useEffect } from "react";
import { Typography } from 'antd';


import { Container, Row, Col, Table } from "react-bootstrap";

import DropdownBtn from "../../Components/TimesheetsDropdownBtn/TimesheetsDropdownBtn";
import Loading from "../../Components/Loading/Loading";

const { Text, Link } = Typography;

const mockupTableData = [
  {
    id: 1,
    number: "00001",
    customer: "Hassan Juma",
    name: "Rob Janssen",
    period: "08-01-2024 - 15-01-2024",
    hours: 12,
    status: "Draft",
    attachment: true,
  },
  {
    id: 2,
    number: "00002",
    customer: "john doe",
    name: "robert janssen",
    period: "08-01-2024 - 15-01-2024",
    hours: 36,
    status: "Draft",
    attachment: false,
  },
  {
    id: 3,
    number: "00003",
    customer: "imran",
    name: "christopher",
    period: "01-01-2024 - 08-01-2024",
    hours: 5,
    status: "Invoiced",
    attachment: false,
  },
];

function Timesheets() {
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Simulate API call
    setTimeout(() => {
      setIsLoading(false);
    }, 0); // Set to 2000 to simulate 2 seconds of loading time
  }, []);

  const timesheetTableData = mockupTableData.map((timesheet) => (
    <tr key={timesheet.id}>
      <td>
        <Link href={`timesheets/${timesheet.id}`}>{timesheet.number}</Link>
      </td>
      <td>{timesheet.customer}</td>
      <td>{timesheet.name}</td>
      <td>{timesheet.period}</td>
      <td>{timesheet.hours}</td>
      <td className={timesheet.status === 'Invoiced' ? 'invoiced' : ''} >{timesheet.status}</td>
      <td>{timesheet.attachment ? "Yes" : "No"}</td>
      <td>
        <DropdownBtn
          variant={"warning"}
          title={"Actions"}
          size={"sm"}
          timesheetKey={timesheet.id}
        />
      </td>
    </tr>
  ));

  if (isLoading) {
    return (
      <div className="timesheets">
        <div className="titleblock">
          <h3>Timesheets</h3>
        </div>
        <Loading />
      </div>
    );
  }

  return (
    <div className="timesheets">
      <div className="titleblock">
        <h3>Timesheets</h3>
      </div>
      <Container className="content">
        <Row>
          <Col>
            <Text>Space for filter (search & filters).</Text>
            <Table responsive="sm" hover striped>
              <thead>
                <tr>
                  <th>Number</th>
                  <th>Customer</th>
                  <th>Name</th>
                  <th>Period</th>
                  <th>Hours</th>
                  <th>Status</th>
                  <th>Attachment</th>
                  <th></th>
                </tr>
              </thead>
              <tbody id="timesheetsTable">{timesheetTableData}</tbody>
            </Table>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Timesheets;
