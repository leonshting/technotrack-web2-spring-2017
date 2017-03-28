export const userReceived = (state, action) => {
    if(state === undefined) {
        return {user_id: -1, username: '', email: '', lastUpdated: 0};
    }

    switch (action.type) {
        case 'RECEIVE_USER':
            return Object.assign({}, state,
                {
                    user_id_fetched: action.user_id,
                    username: action.username,
                    email: '',
                    lastUpdated: action.receivedAt
                });
        default:
            return state;
    }
};