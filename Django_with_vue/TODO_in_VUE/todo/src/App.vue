<template>
  <H3>MY TODO APP</H3>
  <TaskNew v-for="task in tasks" :key="task.id" :task="task"></TaskNew>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import axios from 'axios';
import TaskNew from './components/Task.vue'
export default {
  name: 'App',
  components: {
    TaskNew
  },
  data: () => {
    return{
      msg: "Hello Kumkum!", 
      tasks: [
    ]
    }
    
  },
  created() {
    axios.get('http://127.0.0.1:8000/tasks/')
      .then(response => {
        this.tasks = response.data;
      })
      .catch(error => {
        console.error(error);
      });
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
