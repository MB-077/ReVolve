import React from 'react';
import { motion } from 'framer-motion';
import Breadcrumb from '../components/Breadcrumb';

const Results = ({ data }) => {
  return (
    <div className="min-h-screen bg-gray-100 p-5">
      <Breadcrumb />
      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
        {data.map((item, index) => (
          <div key={index} className="bg-white p-5 rounded-lg shadow-lg">
            <img src={item.image} alt={item.company_name} className="w-full h-40 object-cover mb-3 rounded" />
            <h3 className="text-xl font-bold mb-2">{item.company_name}</h3>
            <p className="text-gray-700 mb-2">{item.description}</p>
            <p className="text-gray-900 font-bold">${item.estimated_cost}</p>
          </div>
        ))}
      </motion.div>
    </div>
  );
};

export default Results;
