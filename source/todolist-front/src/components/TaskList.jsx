import React, { Component } from 'react';


export default class TaskList extends Component {
    render() {
        if (this.props.task_list.length === 0) {
            return (
                <div>タスク無し</div>
            );
        }
        const items = this.props.task_list.map((obj, index) => {
            return (
                <div key={index}>{obj.id}: {obj.content}</div>
            );
        });

        return (
            <div>{items}</div>
        );
    };
}
