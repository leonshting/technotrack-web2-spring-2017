import {Button, ButtonGroup} from 'react-bootstrap';
import React from 'react';

class VerticalButtonBlock extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            locked:true
        };
    }

    componentWillReceiveProps = (nextProps) => {
        console.log(nextProps);
        this.setState(
            {
                locked: nextProps.locked,
            }
        );
    };

    render() {
        const buttons = [
            <Button disabled={this.state.locked} key={ 1 } onClick={this.props.onMyPageClick}>My Page</Button>,
            <Button disabled={this.state.locked} key={ 2 } onClick={this.props.onFeedClick}>Feed</Button>,
            <Button disabled={this.state.locked} key={ 3 } onClick={this.props.onChatClick}>Chats</Button>
        ];

        return (<ButtonGroup vertical>
            { buttons }
        </ButtonGroup>);
    }
}

VerticalButtonBlock.propTypes = {
    onMyPageClick: React.PropTypes.func,
    onFeedClick: React.PropTypes.func,
    onChatClick: React.PropTypes.func,
};
export default VerticalButtonBlock;