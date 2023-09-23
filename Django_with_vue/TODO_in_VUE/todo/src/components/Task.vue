<template>
  <div class="box" :class="task.priority?'priority_task':'normal_task'">
    <p>{{ task.title }}</p>
    <img v-show="task.completed" src="../assets/icon_tick.png" style="width: 20px; height: 20px;" alt="">
    <button v-on:click="set_as_completed(task)">Completed</button>
    <button>Deleted</button>
    <button @click="set_as_priority(task)">Set as priority</button>
  </div>

</template>

<script>
export default {
    name: 'TaskNew',
    props: ["task"],
    methods:{
        set_as_priority(task) {
            task.priority = !task.priority
            console.log("task set as priority")
        },
        set_as_completed(task){
            task.completed = !task.completed
        }
    }
}
</script>

<style>
    .box{
        width: 300px;
        border:2px;
        background-color: aqua;
    }
    .box.priority_task {
        background-color: yellow;
    }
</style>