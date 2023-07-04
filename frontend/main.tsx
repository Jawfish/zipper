import './index.scss';
import { ToastContainer } from 'react-toastify';
import React from 'react';
import ReactDOM from 'react-dom/client';

import App from './App';

ReactDOM.createRoot(document.querySelector('#root')!).render(
  <React.StrictMode>
    <ToastContainer />
    <App />
  </React.StrictMode>
);
