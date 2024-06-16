import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import "bootstrap/dist/css/bootstrap.min.css";
import "./UI/CSS/shared.css"
import Header from "./UI/Header";
import Footer from "./UI/Footer";

import Dashboard from './Pages/Dashboard/Dashboard'
import Timesheets from './Pages/Timesheets/Timesheets';
import Customers from './Pages/Customers/Customers';
import NewTimesheet from './Pages/NewTimesheet/NewTimesheet'

function App() {
  return (
    <Router>
      <Header />
      <Routes>
        <Route exact path="/" element={<Dashboard />} />
        <Route exact path="/timesheets" element={<Timesheets />} />
        <Route exact path="/settings/editcustomers" element={<Customers />} />
        <Route exact path="/newtimesheet" element={<NewTimesheet />} />
      </Routes>
      <Footer />
    </Router>
  );
}

export default App;
