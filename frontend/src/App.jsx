import { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import PrivateRoute from './components/PrivateRoute';
import Login from './pages/Login';
import SelectAction from './pages/SelectAction';
import Buy from './pages/Buy';
import Results from './pages/Results';
import Sell from './pages/Sell';
import Signup from './pages/Signup'; 

const App = () => {
  const [results, setResults] = useState([]);

  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/signup" element={<Signup />} /> {/* Add route for signup */}
          <Route path="/select" element={<PrivateRoute><SelectAction /></PrivateRoute>} />
          <Route path="/buy" element={<PrivateRoute><Buy onResults={setResults} /></PrivateRoute>} />
          <Route path="/results" element={<PrivateRoute><Results data={results} /></PrivateRoute>} />
          <Route path="/sell" element={<PrivateRoute><Sell /></PrivateRoute>} />
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;
