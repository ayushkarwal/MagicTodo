<template>
  
  <form @submit.prevent="add_task">
    <h2 class="tasks-heading">Add new task:</h2>
    <label>Title:</label>
    <input type="text" v-model="title" >
    <br>
    <label>Is it a priority task?</label>
    <input type="checkbox" v-model="priority">
    <br>
    <label>Due Date:</label>
    <input type="datetime-local" id="datetime" name="datetime" v-model="complete_on">
    <button class="login-button" >Add Task</button>
    <button type="button" class="login-button" @click="back">Back</button>
  </form>
</template>

<script>
import axios from 'axios';
export default {
    props:['id'],
    data(){
        return{
            title: "",
            priority: false,
            complete_on: null
        }
    },
    methods: {
        add_task(){
            let url = "http://127.0.0.1:8000/tasks/";
            let content = {
                title: this.title,
                created_by: this.id,
                priority: this.priority,
                completed_on: this.complete_on,
            }
            axios.post(url, content)
            .then(response => {
                let data = response.data
                console.log(data.msg)
                console.log(response)
                this.$router.push({name: 'tasks', params:{id: this.id}})
            })
            .catch(error => {
                console.error(error);
            });
            console.log(this.title)
            console.log(this.priority)
            console.log(this.complete_on)

        },
        back(){
            this.$router.go(-1);
        }
    }

}
</script>

<style>
    input[type="checkbox"] {
        margin-left: 100px;
    }
</style>