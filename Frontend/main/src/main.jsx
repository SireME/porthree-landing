import React from 'react'
import ReactDOM from 'react-dom/client'
import Root from './routes/root.jsx'
import Sign from './routes/Sign.jsx'
import Portfolio from './routes/Portfolio.jsx'
import ErrorPage from "./error-page";
import {
  createBrowserRouter,
  RouterProvider,
} from "react-router-dom";
import './index.css'


const router = createBrowserRouter([
  {
    path: "/",
    element: <Root />,
    errorElement: <ErrorPage />,
  },
  {
    path: "sign-up",
    element: <Sign />,
  },
  {
    path: "user",
    element: <Portfolio />,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* <App /> */}
    <RouterProvider router={router} />
  </React.StrictMode>,
)
