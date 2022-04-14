import React from "react";
import { Navigate, Route, RouteProps, Outlet } from "react-router";
import { useSelector } from "react-redux";
import { RootState } from "../store";

const ProtectedRoute = (props: RouteProps) => {
    const auth = useSelector((state: RootState) => state.auth);
    return auth.account ? <Outlet /> : <Navigate to="/login" />;
};

export default ProtectedRoute;