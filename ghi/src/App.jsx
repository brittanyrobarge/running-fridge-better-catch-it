// import Nav from './components/Nav'
// import React from 'react'
// import { Outlet } from 'react-router-dom'
// import Home from './pages/Home'
// import Login from './pages/Login'
// import Home from './pages/SignUp'
// import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";

import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import SignUp from './pages/SignUp'; // Fix the import statement
import Nav from './components/Nav'
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";

function App() {
  // other stuff, here

  return (
      <AuthProvider>
          <Nav />
          <Routes>
              <Route index element={<Home />} />
              <Route path="/login" element={<Login />} />
              <Route path="/signUp" element={<SignUp />} />
          </Routes>
      </AuthProvider>
  )
}

export default App;
