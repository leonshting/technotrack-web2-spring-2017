import React, { Component, PropTypes } from 'react';
import { Button, Form, FormControl, FormGroup } from 'react-bootstrap';
import { doLogin } from '../actions/LoginActions.jsx'
import {connect} from 'react-redux';

class Login extends Component {

    render() {
        const {errorMessage} = this.props;

        return (
            <Form inline>
                <FormGroup controlId="formInlineEmail">
                    <FormControl ref="username" placeholder="Username" onChange={this.handleLoginChange}/>
                </FormGroup>
                <FormGroup controlId="formInlinePassword">
                    <FormControl type="password" ref="password" onChange={this.handlePassChange}/>
                </FormGroup>
                <Button type="submit" onClick={(event) => this.handleClick(event)}>
                    Login
                </Button>
                {errorMessage &&
                <p style={{color:'red'}}>{errorMessage}</p>
                }
            </Form>
        )
    }

    handlePassChange = (e) => {
        this.setState({password: e.target.value});
    };

    handleLoginChange = (e) => {
        this.setState({username: e.target.value});
    };

    handleClick = (event) => {
        event.preventDefault();
        const username = this.state.username;
        const password = this.state.password;
        const creds = { username: username.trim(), password: password.trim() };
        this.props.dispatch(doLogin(creds));

    }
}

Login.propTypes = {
    errorMessage: PropTypes.string
};

Login = connect()(Login);
export default Login;