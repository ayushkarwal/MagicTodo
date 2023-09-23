<template>
  <H3>MY TODO APP</H3>
  <TaskNew v-for="task in tasks" :key="task.id" :task="task"></TaskNew>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
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
      {
        id:1,
        title: "Task 1",
        priority: true,
        completed: false,
      },
      {
        id:2,
        title: "Task 2",
        priority: true,
        completed: false,
      },
      { id:3,
        title: "Task 3",
        priority: false,
        completed: false,
      }
    ]
    }
    
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
