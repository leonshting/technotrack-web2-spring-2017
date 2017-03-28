import fetch from 'isomorphic-fetch'
import {showFeed} from '../../Layout/actions/LayoutActions.jsx'

export function doLogin(creds) {

    return function (dispatch) {
        const headers = new Headers();
        headers.append('Content-Type', 'application/json; charset=utf-8');
        return fetch(`/rest-auth/login/`,
            {
                headers: headers,
                method: 'POST',
                body: JSON.stringify(creds)
            })
            .then(response => {
                return ({ok: response.ok, json: response.json(), username: creds.username})
            })
            .then(object => {
                console.log(object);
                if (object.ok) {
                    dispatch(loginSuccessful(object.username, object.json))
                } else {
                    dispatch(loginFailed(object.username, object.json));
                }
            })
            .then(() => dispatch(showFeed()));
    }
}

export function loginSuccessful(username, json) {
    return {
        type: 'LOGIN_SUCCESSFUL',
        user: username,
        token: json.key,
        id: json.user,
    }
}

export function loginFailed(username, json) {
    console.log(json);
    return {
        type: 'LOGIN_FAILED',
        user: '',
        token: '',
        id: -1,
    }
}