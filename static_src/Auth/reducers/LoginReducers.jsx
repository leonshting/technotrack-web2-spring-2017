import React from 'react'

export const logOnHandle = (state, action) => {
    if (state === undefined) {
        return {logon: false, username: '', token: '', id: -1};
    }

    switch (action.type) {
        case 'LOGIN_SUCCESSFUL':
            return Object.assign({}, state, {logon: true, username: action.user, token: action.token, id: action.id});
        case 'LOGIN_FAILED':
            return Object.assign({}, state, {logon: false, username: '', token: '', id: -1});
        default:
            return state;
    }
};