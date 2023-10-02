<template>
  <div class="box" :class="{'priority_task': task.priority, 'completed_task': task.completed}">
    <p>{{ task.title }}</p>
    <button class="login-button" v-on:click="set_as_completed(task)">{{completed_button}}</button>
    <button class="login-button" @click="delete_task(task)">Deleted</button>
    <button class="login-button" @click="set_as_priority(task)">Set as priority</button>
    <img v-show="task.completed" src="../../assets/icon_tick.png" style="width: 20px; height: 20px;" alt="">
  </div>

</template>

<script>
import axios from 'axios';
export default {
    name: 'TaskNew',
    props: ["task"],
    data(){
        return {
            completed_button : this.task.completed?"Not Complete":"Complete"
        }
    },
    methods:{
        set_as_priority(task) {
            task.priority = !task.priority
            var priority = task.priority
            axios.patch('http://127.0.0.1:8000/tasks/'+task.id+'/', {"priority": priority})
            .then(response => {
                console.log(response.data.id);
            })
            .catch(error => {
                console.error(error);
            });
            console.log("task set as priority")
        },
        set_as_completed(task){
            this.task.completed = !this.task.completed
            this.completed_button = this.task.completed?"Not Complete":"Complete"
            var completed = this.task.completed
            axios.patch('http://127.0.0.1:8000/tasks/'+task.id+'/', {"completed": completed})
            .then(response => {
                console.log(response.data.id);
            })
            .catch(error => {
                console.error(error);
            });
        },
        delete_task(task){
            axios.delete('http://127.0.0.1:8000/tasks/'+task.id+'/')
            .then(response => {
                location.reload()
                console.log(response.data.id);
            })
            .catch(error => {
                console.error(error);
            });
        }
    }
}
</script>

<style>
    .box {
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    padding: 10px;
    margin: 10px 0;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    /* Styles for priority tasks */
    .priority_task {
    background-color: #ffea9d; /* Yellow background for priority tasks */
    border: 1px solid #ffc107; /* Border color for priority tasks */
    }

    .completed_task {
    background-color: #17e593; /* Yellow background for priority tasks */
    border: 1px solid #019a3c; /* Border color for priority tasks */
    }

    /* Styles for normal tasks */
    .normal_task {
    background-color: #f0f0f0; /* Default background for normal tasks */
    border: 1px solid #ccc; /* Default border color for normal tasks */
    }

    /* Styles for task titles */
    .box p {
    font-size: 18px;
    font-weight: bold;
    color: #333;
    margin: 0;
    }

    /* Styles for the completed task icon */
    .box img {
    width: 20px;
    height: 20px;
    margin-left: 5px;
    vertical-align: middle;
    }
</style>