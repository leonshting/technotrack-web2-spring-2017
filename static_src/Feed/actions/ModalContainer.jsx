export const openModal = (element) => {
    return {
        type: 'OPEN_MODAL',
        element: element
    }
};

export const closeModal = () => {
    return {
        type: 'CLOSE_MODAL'
    }
};

