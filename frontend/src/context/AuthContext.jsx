import React, { createContext, useState, useContext, useEffect } from 'react';

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const storedAuth = localStorage.getItem('isAuthenticated');
    if (storedAuth) {
      setIsAuthenticated(JSON.parse(storedAuth));
    }
  }, []);

  const login = (rememberMe) => {
    setIsAuthenticated(true);
    if (rememberMe) {
      localStorage.setItem('isAuthenticated', true);
    }
  };

  const logout = () => {
    setIsAuthenticated(false);
    localStorage.removeItem('isAuthenticated');
  };

  const signup = () => {
    // Implement signup logic here, such as sending data to backend
    // For simplicity, we are not implementing actual signup logic in this example
    // You may need to modify this function to handle signup
    setIsAuthenticated(true); // Auto login after signup for simplicity, you may modify this logic
    localStorage.setItem('isAuthenticated', true);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, login, logout, signup }}>
      {children}
    </AuthContext.Provider>
  );
};
