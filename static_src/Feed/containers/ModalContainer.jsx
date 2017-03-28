import {connect} from 'react-redux'
import {openModal, closeModal} from '../actions/ModalContainer.jsx'
import ModalContainer from '../components/ModalContainer.jsx'
import React from 'react'

const mapStateToProps = (state) => {
    let opened = undefined;
    if (state.modalVisibilityReducer.showModal) {
        opened = true;
    } else {
        opened = false;
    }
    let element = state.modalVisibilityReducer.modal_element;
    return {
        opened: opened,
        element: element
    }
};

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onOpenModal: () => {
            dispatch(openModal(ownProps.element))
        },
        onCloseModal: () => {
            dispatch(closeModal())
        }
    }
};

const VisibleModalContainer = connect(mapStateToProps, mapDispatchToProps)(ModalContainer);
export default VisibleModalContainer;


