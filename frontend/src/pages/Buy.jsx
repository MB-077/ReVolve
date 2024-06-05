import  { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import Breadcrumb from '../components/Breadcrumb';

const Buy = ({ onResults }) => {
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSend = async () => {
    setLoading(true);
    try {
      const response = await axios.post('/api/buy', { prompt: input });
      onResults(response.data);
      navigate('/results');
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <Breadcrumb />
      {loading ? (
        <div className="fixed inset-0 flex items-center justify-center bg-gray-900 bg-opacity-75">
          <div className="loader"></div>
        </div>
      ) : (
        <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
          <h2 className="text-2xl font-bold mb-5">Welcome to Re-Volve</h2>
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            className="border p-2 mb-3 w-full"
            rows="5"
            placeholder="How can we help You?"
          />
          <button onClick={handleSend} className="bg-blue-500 text-white p-2 rounded">Send</button>
        </motion.div>
      )}
    </div>
  );
};

export default Buy;
