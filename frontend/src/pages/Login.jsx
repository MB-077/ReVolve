import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const Login = () => {
  const navigate = useNavigate();
  const { login } = useAuth();
  const [rememberMe, setRememberMe] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    login(rememberMe);
    navigate('/select');
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded-lg shadow-lg">
        <h2 className="text-2xl font-bold mb-5">Login</h2>
        <input
          type="text"
          placeholder="Username"
          className="border p-2 mb-3 w-full"
          required
        />
        <input
          type="password"
          placeholder="Password"
          className="border p-2 mb-3 w-full"
          required
        />
        <div className="flex items-center mb-4">
          <input
            type="checkbox"
            checked={rememberMe}
            onChange={() => setRememberMe(!rememberMe)}
            className="mr-2"
          />
          <label>Remember Me</label>
        </div>
        <button type="submit" className="bg-blue-500 text-white p-2 w-full rounded">Login</button>
        <p className="mt-2 text-gray-600">Don't have an account? <Link to="/signup" className="text-blue-500 hover:underline">Sign up here</Link></p>
      </form>
    </div>
  );
};

export default Login;
