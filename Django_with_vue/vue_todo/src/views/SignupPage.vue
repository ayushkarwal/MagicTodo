<template>
  <form @submit.prevent="create_new_user">
    <label>First Name:</label>
    <input type="text" v-model="first_name">
    <br>
    <label>Last Name:</label>
    <input type="text" v-model="last_name">
    <br>
    <label>Email:</label>
    <input type="email" v-model="email">
    <br>
    <label>Password:</label>
    <input type="password" v-model="password">
    <br>
    <label>Confirm Password:</label>
    <input type="password" v-model="confirm_password">
    <br>
    <button class="login-button">Sign UP</button>
    <button type="button" class="login-button" @click="back">Back</button>
    <p class="error" v-if="show_error">Invalid details!</p>
  </form>
</template>

<script>
import axios from 'axios';
export default {
  data (){
    return {
      first_name : "",
      last_name: "",
      email: "",
      password: "",
      confirm_password: "",
      show_error : false
    }
  },
  methods: {
    create_new_user(){
      let url = "http://127.0.0.1:8000/users/"
      let content = {
        "email": this.email,
        "password": this.password,
        "first_name": this.first_name,
        "last_name": this.last_name,
        "username": this.first_name.toLowerCase() + "_" + this.last_name.toLowerCase()
      }
      axios.post(url, content)
      .then(response => {
        let data = response.data
        console.log(response)
        this.$router.push({name: 'tasks', params:{id: data.id}})
      })
      .catch(error => {
        console.error(error);
        show_error = true
      });
    },
    back(){
      this.$router.go(-1);
    }
  }

}
</script>

<style>
    form {
        max-width: 420px;
        border-radius: 10px;
        margin: 30px auto;
        background: white;
        text-align: left;
        padding: 40px;
    }
    label {
        color: #aaa;
        display: inline-block;
        margin: 25px 0 15px;
        font-size: 0.6em;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: bold;
    }
    input, select {
        display: block;
        padding: 10px 6px;
        width: 100%;
        box-sizing: border-box;
        border: none;
        border-bottom: 1px solid #ddd;
        color: #555;
    }
    input[type="checkbox"] {
        display: inline-block;
        position: relative;
        width: 16px;
        margin: 0 10px 0 0;
        top: 2px;
    }
    .pill {
        display: inline-block;
        margin: 20px 10px 0 0;
        padding: 6px 12px;
        background: #eee;
        border-radius: 20px;
        font-size: 12px;
        letter-spacing: 1px;
        font-weight: bold;
        color: #777;
        cursor: pointer;
    }
    button {
        background: #0b6dff;
        border: 0;
        padding: 10px 20px;
        margin-top: 20px;
        color: white;
        border-radius: 20px;
        margin-left: 5px;
    }
    .submit{
        text-align: center;
    }

    .error {
        color: #ff0062;
        margin-top: 10px;
        font-size: 0.8em;
        font-weight: bold;
    }
  </style>