import fetch from 'isomorphic-fetch'
const base64 = require('base-64');



function requestUser(id) {
    return {
        type: 'REQUEST_USER',
        user_id: id,
    }
}

function receiveUser(id, json) {
    console.log(json);
    return {
        type: 'RECEIVE_USER',
        user_id: id,
        username: json.username,
        receivedAt: Date.now()
    }
}


export function fetchUser(id) {

    return function (dispatch) {

        dispatch(requestUser(id));

        const headers = new Headers();
        headers.append("Authorization", "Basic " + base64.encode("admin:getitnow"));

        return fetch(`/api/user/${id}`, {headers: headers})
            .then(response => response.json())
            .then(json => dispatch(receiveUser(id, json))
            );
    }
}