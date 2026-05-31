import { Routes, Route } from "react-router-dom";

import Landing from "./pages/Landing";
import DesignMode from "./pages/DesignMode";
import AdvisorMode from "./pages/AdvisorMode";


function App() {
  return (
    <Routes>
      <Route path="/" element={<Landing />} />
      <Route path="/design" element={<DesignMode />} />
      <Route path="/advisor" element={<AdvisorMode />} />
      
    </Routes>
  ); 
}

export default App;
