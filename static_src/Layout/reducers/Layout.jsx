export const showWindow = (state, action) => {
    if (state === undefined) {
        return {currently_shown: ''};
    }

    switch (action.type) {
        case 'SHOW_LOGIN':
            return Object.assign({}, state, {currently_shown: 'login'});
        case 'SHOW_FEED':
            return Object.assign({}, state, {currently_shown: 'feed'});
        case 'SHOW_MYPAGE':
            return Object.assign({}, state, {currently_shown: 'mypage'});
        case 'SHOW_CHATS':
            return Object.assign({}, state, {currently_shown: 'chats'});
        case 'SHOW_CHAT':
            return Object.assign({}, state, {currently_shown: 'chat'});
        default:
            return state;
    }
};
