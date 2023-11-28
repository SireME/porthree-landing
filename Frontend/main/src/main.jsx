import React from 'react'
import ReactDOM from 'react-dom/client'
import Root from './routes/root'
import Sign from './routes/Sign'
import Portfolio from './routes/Portfolio'
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
    children: [
      {
        path: "sign-up",
        element: <Sign />,
      },
    ],
  },
  {
    path: "Portfolio/:userId",
    element: <Portfolio />,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* <App /> */}
    <RouterProvider router={router} />
  </React.StrictMode>,
)
