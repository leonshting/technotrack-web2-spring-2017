/**
 * Created by leonshting on 26.03.17.
 */
import React from 'react';
import {Button, ButtonGroup} from 'react-bootstrap';

import {listCookies} from '../../utils.js';

class HeaderUser extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            logon: false,
            username: ''
        };
    }

    componentWillReceiveProps = (nextProps) => {
        console.log(nextProps);
        this.setState(
            {
                logon: nextProps.logon,
                username: nextProps.username,
            }
        );
    };

    render() {
        let element = undefined;
        if (this.state.logon) {
            element =
                <ButtonGroup id="user-log">
                    <Button id="username">{ this.state.username }</Button>
                    <Button>Q</Button>
                </ButtonGroup>;
        }
        else {
            element =
                <ButtonGroup id="user-log">
                    <Button id="login" onClick={this.props.onLoginClick}> Login </Button>
                </ButtonGroup>
        }
        return element;
    }
}

HeaderUser.propTypes = {
    onLoginClick: React.PropTypes.func.isRequired,
    //onQCLick
};

export default HeaderUser;