<template>
  <div class="container">
    <h3 class="intro">Welcome to Magic TODO</h3>
    <div class="buttons">
      <button class="login-button" @click="login">Login</button>
      <p>Already a user?</p>
      <button class="signup-button" @click="signup">Sign Up</button>
      <p>New to MagicTODO?</p>
    </div>
    <!-- 
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>
    -->
  </div>
  
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'

export default {
  methods: {
    login() {
      this.$router.push('/login')
    },
    signup() {
      this.$router.push('/signup')
    }
  }
  
}
</script>
<style>
  /* Style the container (optional) */
  /* .container {
    text-align: center;
    background-color: #3498db;
    padding: 20px;
    border-radius: 5px;
  } */

  /* Style the heading */
  
</style>