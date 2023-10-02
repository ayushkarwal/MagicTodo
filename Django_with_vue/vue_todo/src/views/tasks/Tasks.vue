<template>
    <h2 class="tasks-heading" v-show="tasks.length">My Tasks:</h2>
    <h2 class="tasks-heading" v-show="!tasks.length"> You have no tasks.</h2>
  <TaskNew v-for="task in tasks" :key="task.id" :task="task"></TaskNew>
  <button type="button" class="login-button" @click="add_new_task">Add New Task</button>
  <button type="button" class="login-button top-right-button" @click="logout">Log out</button>
</template>

<script>
import TaskNew from '../tasks/Task.vue'
import axios from 'axios';
export default {
    props:['id'],
    data(){
        return {
            tasks : []
        }
    },
    created() {
        let url = "http://127.0.0.1:8000/users/" + this.id + "/get_tasks/"
        axios.get(url)
        .then(response => {
            this.tasks = response.data;
        })
        .catch(error => {
            console.error(error);
        });
    },
    components: {
        TaskNew
    },
    methods: {
        logout(){
            this.$router.push({name: 'welcome'})
        },
        add_new_task(){
            this.$router.push({name: 'addtask', params:{id: this.id}})
        }
    }
}
</script>

<style>
    h2.tasks-heading {
    font-size: 24px; /* Customize the font size as needed */
    font-weight: bold; /* Customize the font weight as needed */
    color: #333; /* Customize the text color as needed */
    margin-bottom: 10px; /* Add margins as needed */
    }
</style>