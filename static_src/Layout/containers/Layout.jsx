import {connect} from 'react-redux'
import Layout from '../components/Layout.jsx'
import React from 'react'

const mapStateToProps = (state) => {
    return {
        currently_shown: state.showWindow.currently_shown,
    }
};

const VisibleLayout = connect(mapStateToProps)(Layout);
export default VisibleLayout;