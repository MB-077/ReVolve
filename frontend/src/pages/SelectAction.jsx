import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import Breadcrumb from '../components/Breadcrumb';

const SelectAction = () => {
  const navigate = useNavigate();
  const { logout } = useAuth();

  const handleSelect = (action) => {
    navigate(`/${action}`);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100">
      <Breadcrumb />
      <h2 className="text-2xl font-bold mb-5">What would you like to do today?</h2>
      <button onClick={() => handleSelect('buy')} className="bg-green-500 text-white p-2 m-2 rounded">Buy</button>
      <button onClick={() => handleSelect('sell')} className="bg-red-500 text-white p-2 m-2 rounded">Sell</button>
      <button onClick={() => { logout(); navigate('/'); }} className="bg-gray-500 text-white p-2 m-2 rounded">Logout</button>
    </div>
  );
};

export default SelectAction;
