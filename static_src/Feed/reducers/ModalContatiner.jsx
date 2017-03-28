import React from 'react'

const modalVisibilityReducer = (state, action) => {
    if(state === undefined) {
        return {showModal: false, modal_element: null};
    }

    switch(action.type) {
        case 'OPEN_MODAL':
            return Object.assign({}, state, {showModal: true, modal_element: action.element});
        case 'CLOSE_MODAL':
            return Object.assign({}, state, {showModal: false, modal_element: null});
        default:
            return state;
    }
};

export default modalVisibilityReducer;
