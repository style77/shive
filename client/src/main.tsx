import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import {
  createBrowserRouter,
  RouterProvider
} from "react-router-dom"
import Login from './pages/Login.tsx'
import Dashboard from './pages/Dashboard.tsx'

const router = createBrowserRouter([
  {
      path: "/",
      element: <App />,
  },
  {
      path: "/login",
      element: <Login />,
  },
  {
    path: "/dashboard",
    element: <Dashboard />
  },
]);

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
