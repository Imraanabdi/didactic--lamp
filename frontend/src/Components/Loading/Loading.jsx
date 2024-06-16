import './Loading.css'
import React from "react";
import { Spin } from "antd";

const Loading = () => {
  return (
    <div className="spinner">
      <Spin size="large" />
    </div>
  );
};

export default Loading;
