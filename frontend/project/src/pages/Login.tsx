import React, { useState } from "react";
import * as Yup from "yup";
import { useFormik } from "formik";
import { useDispatch } from "react-redux";
import axios from "axios";
import { useNavigate } from "react-router";
import { 
    Avatar, Button, CssBaseline, FormHelperText, TextField, FormControlLabel, 
    Checkbox, Link, Grid, Box, Typography, Container
} from '@mui/material';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import authSlice from "../store/slices/auth";


const theme = createTheme();

function Login(){
    const [message, setMessage] = useState("");
    const [loading, setLoading] = useState(false);
    const dispatch = useDispatch();
    const navigate = useNavigate();

    const handleLogin = (email: string, password: string) => {
        axios
        .post(`${process.env.REACT_APP_API_URL}/core/auth/login/`, { email, password })
        .then((res) => {
            dispatch(
                authSlice.actions.setAuthTokens({
                    token: res.data.access,
                    refreshToken: res.data.refresh,
                })
            );
            dispatch(authSlice.actions.setAccount(res.data.user));
            setLoading(false);
                navigate("/");
        })
        .catch((err) => {
            setMessage(err.response.data.detail.toString());
        });
    };

    const formik = useFormik({
        initialValues:{
            email: "",
            password: "",
        },
        onSubmit: (values)=>{
            setLoading(true);
            handleLogin(values.email, values.password);
        },
        validationSchema: Yup.object({
            email: Yup.string().trim().required('Email is required'),
            password: Yup.string().trim().required("Password is required"),

        })
    });

    return(
        <ThemeProvider theme={theme}>
            <Container component="main" maxWidth="xs">
                <CssBaseline />
                <Box
                    sx={{
                        marginTop: 8,
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center'
                    }}
                >
                    <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
                        <LockOutlinedIcon />
                    </Avatar>
                    <Typography component="h1" variant="h5">
                        Sign in
                    </Typography>
                    <Box component="form" onSubmit={formik.handleSubmit} noValidate sx={{ mt: 1 }}>
                        <TextField
                            error={formik.errors.email?true:false}
                            margin="normal"
                            required
                            fullWidth
                            id="email"
                            label="Email Address"
                            name="email"
                            autoComplete="email"
                            value={formik.values.email}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                            autoFocus
                            helperText={formik.errors.email}
                        />
                        <TextField
                            error={formik.errors.password?true:false}
                            margin="normal"
                            required
                            fullWidth
                            name="password"
                            label="Password"
                            type="password"
                            id="password"
                            value={formik.values.password}
                            onChange={formik.handleChange}
                            onBlur={formik.handleBlur}
                            autoComplete="current-password"
                            helperText={formik.errors.password}
                        />
                        <FormHelperText id="formResult" children={message?message:' '}/>
                        <Button
                            type="submit"
                            fullWidth
                            variant="contained"
                            sx={{ mt: 3, mb: 2 }}
                        >
                            Sign In
                        </Button>
                    </Box>
                </Box>
            </Container>
        </ThemeProvider>
    );
}

export default Login;
