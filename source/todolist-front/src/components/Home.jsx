import React, { Component } from 'react';
import axios from 'axios';
import AddForm from './AddForm';
import TaskList from './TaskList';

const endpoint_url = 'http://192.168.33.10:8000/task'


export default class Home extends Component {

    constructor(props) {
        super(props);
        this.state = {
            task_list: []
        };
        this.getTasks = this.getTasks.bind(this);
        this.createTask = this.createTask.bind(this);
    }

    getTasks() {
        axios
            .get(endpoint_url + '/')
            .then((res) => {
                this.setState({
                    task_list: res.data
                });
            })
            .catch((error) => {
                console.log(error);
            });
    }

    createTask(content) {
        axios
            .post(endpoint_url + '/create', {
                content: content
            })
            .then((res) => {
                console.log(res.data);
                this.getTasks();
            })
            .catch((error) => {
                console.log(error);
            });
    }

    componentDidMount = () => {
        this.getTasks();
    }

    render() {
        return (
            <div>
                <AddForm createTask={this.createTask} />
                <TaskList task_list={this.state.task_list} />
            </div>
        );
    }

}
