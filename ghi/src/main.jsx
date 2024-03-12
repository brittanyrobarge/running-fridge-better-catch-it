import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import { createBrowserRouter, RouterProvider } from "react-router-dom"
import Login from './pages/Login'
import Home from './pages/Home'
import SignUp from './pages/SignUp'



const router = createBrowserRouter([
    {
        path: "/",
        element: <App />,
        children: [
            {index: true, element: <Home />},
            {path: "login", element: <Login />},
            {path: "signUp", element: <SignUp />},
            ]
    },
])

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>

        <RouterProvider router={router} />

    </React.StrictMode>
)
