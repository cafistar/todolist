import React, { Component } from 'react';


export default class AddForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            task: ''
        };
        this.changeTask = this.changeTask.bind(this);
        this.createTask = this.createTask.bind(this);
    }

    changeTask(event) {
        this.setState({
            task: event.target.value
        });
    }

    createTask(event) {
        event.preventDefault();
        console.log(this.state.task);
        if (this.state.task === '') {
            return;
        }
        this.setState({
            task: ''
        });
        this.props.createTask(this.state.task);
    }

    render() {
        return (
            <div>
                <form onSubmit={this.createTask}>
                    <input type="text" name="content" value={this.state.task} onChange={this.changeTask} />
                    <button type="submit">追加</button>
                </form>
            </div>
        );
    }

}
