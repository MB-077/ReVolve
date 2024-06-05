import React, { useState } from 'react';
import axios from 'axios';
import Breadcrumb from '../components/Breadcrumb';

const Sell = () => {
  const [formData, setFormData] = useState({
    company_name: '',
    description: '',
    weight: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/api/sell', formData);
      // Handle successful form submission
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <Breadcrumb />
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-lg">
        <h2 className="text-2xl font-bold mb-5">Sell Scrap</h2>
        <input
          type="text"
          name="company_name"
          placeholder="Company Name"
          value={formData.company_name}
          onChange={handleChange}
          className="border p-2 mb-3 w-full"
          required
        />
        <textarea
          name="description"
          placeholder="Description"
          value={formData.description}
          onChange={handleChange}
          className="border p-2 mb-3 w-full"
          rows="5"
          required
        />
        <input
          type="text"
          name="weight"
          placeholder="Weight"
          value={formData.weight}
          onChange={handleChange}
          className="border p-2 mb-3 w-full"
          required
        />
        <button type="submit" className="bg-blue-500 text-white p-2 w-full rounded">Submit</button>
      </form>
    </div>
  );
};

export default Sell;
