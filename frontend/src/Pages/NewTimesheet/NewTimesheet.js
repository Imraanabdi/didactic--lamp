import React, { useState } from "react";
import { Container, Row, Col } from "react-bootstrap";
import "./NewTimesheet.css";

import { Button, Form, Select, DatePicker, Table } from "antd";
import dayjs from "dayjs";
import "dayjs/locale/nl";
import locale from "antd/es/date-picker/locale/nl_NL";

dayjs.locale("nl");

function Dashboard() {
  const [tableHeaders, setTableHeaders] = useState([]);
  const [selectedDate, setSelectedDate] = useState([]);
  const onFinish = (values) => {
    console.log("Success:", values);
    setTableHeaders([values.customer]);
  };
  const onFinishFailed = (errorInfo) => {
    console.log("Failed:", errorInfo);
  };

  let days = [
    { title: "Project", dataIndex: "project", key: "project", width: "35%" },
  ];
  let curr = new Date(selectedDate);

  for (let i = 1; i <= 7; i++) {
    let first = curr.getDate() - curr.getDay() + i;
    let day = new Date(curr.setDate(first)).toUTCString().slice(0, 16);
    // days.push({title: 'test', children: [{
    //     title: day,
    //     dateIndex: `day${i}`,
    //     key: 'date',
    //     align: 'center',
    // }
    // ]})
    days.push({
      title: day,
      dataIndex: `day${i}`,
      key: "date",
      align: "center",
    });
  }

  days.push({
    title: "Total",
    dataIndex: "total",
    key: "total",
    width: "10%",
    align: "right",
  });

  let rows = [
    {
      key: "project",
      project: "PROJECT: TESTING",
      day1: 8,
      day2: 8,
      day3: 8,
      day4: 8,
      day5: 8,
      day6: 0,
      day7: 0,
    },
  ];

  rows = [
    ...rows,
    {
      key: "project",
      project: "Travel allowance",
    },
  ];

  return (
    <div className="newTimesheet">
      <div className="titleblock">
        <h3>New timesheet</h3>
      </div>
      <Container className="content">
        <Row>
          <Col>
            <Form
              name="basic"
              labelCol={{
                span: 8,
              }}
              wrapperCol={{
                span: 16,
              }}
              style={{
                maxWidth: 600,
              }}
              initialValues={{
                remember: true,
              }}
              onFinish={onFinish}
              onFinishFailed={onFinishFailed}
              autoComplete="off"
            >
              <Form.Item
                label="Customer"
                name="customer"
                rules={[
                  {
                    required: true,
                    message: "Please select a customer.",
                  },
                ]}
              >
                <Select initialvalues={""}>
                  <Select.Option value="First">First</Select.Option>
                  <Select.Option value="2nd">Second</Select.Option>
                </Select>
              </Form.Item>
              <Form.Item
                label="Date range"
                name="date-range"
                rules={[
                  {
                    required: true,
                    message: "Please select a date range.",
                  },
                ]}
              >
                <DatePicker
                  picker="week"
                  format={"YYYY-ww"}
                  locale={locale}
                  onChange={(date, dateString) => {
                    setSelectedDate(date);
                  }}
                  renderExtraFooter={() => "Select the week number"}
                />
              </Form.Item>
              <Form.Item
                label="Engineer/Employee"
                name="employee"
                rules={[
                  {
                    required: true,
                    message: "Please select an employee.",
                  },
                ]}
              >
                <Select>
                  <Select.Option value="1">imran khan</Select.Option>
                  <Select>
                  <Select.Option value="1">imran khan</Select.Option>
                </Select>
                <Select>
                  <Select.Option value="1">imran khan</Select.Option>
                </Select>
                </Select>
              </Form.Item>
              <Form.Item
                wrapperCol={{
                  offset: 8,
                  span: 16,
                }}
              >
                <br></br>
                <Button type="primary" htmlType="submit">
                  Submit
                </Button>
              </Form.Item>
            </Form>
            <br></br>
            <Table
              columns={days}
              dataSource={rows}
              pagination={false}
              bordered={true}
              summary={(pageData) => {
                let totalBorrow = 0;
                let totalRepayment = 0;
        
                pageData.forEach(({ borrow, repayment }) => {
                  totalBorrow += borrow;
                  totalRepayment += repayment;
                });
        
                return (
                  <>
                    <Table.Summary.Row>
                      <Table.Summary.Cell index={0}>Total</Table.Summary.Cell>
                      <Table.Summary.Cell index={1}>
                        {totalBorrow}
                      </Table.Summary.Cell>
                      <Table.Summary.Cell index={2}>
                        {totalRepayment}
                      </Table.Summary.Cell>
                    </Table.Summary.Row>

                  </>
                );
              }}
            />
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default Dashboard;
