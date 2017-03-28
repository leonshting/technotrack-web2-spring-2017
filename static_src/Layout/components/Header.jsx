import React from 'react'
import VisibleHeaderUser from '../containers/HeaderUser.jsx'

class Header extends React.Component {

    render() {
        return (
            <nav className="navbar navbar-inverse">
                <div className="logo-container">
                    <h1>Сеточка</h1>
                </div>
                <VisibleHeaderUser />
            </nav>
        );
    }
}

export default Header;