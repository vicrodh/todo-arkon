import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import store, { persistor } from "./store";
import { PersistGate } from "redux-persist/integration/react";
import { Provider } from "react-redux";
import ProtectedRoute from './routes/ProtectedRoute';



export default function App() {
  return(
    <Provider store={store}>
      <PersistGate persistor={persistor} loading={null}>
        <Router>
          <div>
            {/* <Routes>
              <Route path="/login" element={<Login />} />
              <ProtectedRoute path="/" element={<Dashboard />} />
            </Routes> */}
            <Routes>
              <Route path='/' element={<ProtectedRoute/>}>
                <Route path='/' element={<Dashboard/>}/>
              </Route>
              <Route path='/login' element={<Login/>}/>
            </Routes>
          </div>
        </Router>
      </PersistGate>
    </Provider>
  );
}

