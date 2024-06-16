import React from "react";
import { Dropdown } from "react-bootstrap";

const TimesheetsDropdownBtn = (props) => {
  return (
    <Dropdown>
      <Dropdown.Toggle variant={props.variant} size={props.size}>
        {props.title}
      </Dropdown.Toggle>
      <Dropdown.Menu>
        <Dropdown.Item href={`download/key=${props.timesheetKey}`}>
          Download PDF
        </Dropdown.Item>
        <Dropdown.Item href={`edit/key=${props.timesheetKey}`}>
          Edit
        </Dropdown.Item>
        <Dropdown.Divider></Dropdown.Divider>
        <Dropdown.Item href={`delete/key=${props.timesheetKey}`}>
          Delete
        </Dropdown.Item>
      </Dropdown.Menu>
    </Dropdown>
  );
};

export default TimesheetsDropdownBtn;
