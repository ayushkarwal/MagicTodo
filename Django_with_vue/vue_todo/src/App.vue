<template>
  <router-view/>
</template>

<script>
export default {
  methods: {
    login() {
      this.$router.push('/login')
    }
  }
}
</script>

<style>
  /* Global styles */
  body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
  }

  /* Container for the content */
  .container {
    text-align: center;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
  }

  /* Header style */
  .intro {
    color: #3498db;
    font-size: 24px;
    margin: 0;
  }

  /* Button styles */
  .buttons {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
    margin-top: 20px;
  }

  .login-button,
  .signup-button {
    padding: 10px 20px;
    background: linear-gradient(to bottom, #3498db, #2980b9);
    color: #fff;
    font-size: 16px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
  }

  .login-button:hover,
  .signup-button:hover {
    background: linear-gradient(to bottom, #2980b9, #3498db);
    transform: translateY(-3px);
    box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.2);
  }

  /* Paragraph styles */
  p {
    margin: 10px 0;
    color: #666;
  }
</style>

<!-- <style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.intro{
    color: #3498db;
    font-size: 24px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    margin: 0;
    text-align: center;
    margin-top: 10%;
  }

/* Style for the button */
button {
  display: inline-block;
  padding: 10px 20px;
  background: linear-gradient(to bottom, #3498db, #2980b9);
  color: #ffffff;
  font-size: 14px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease, background 0.2s ease;
  margin: 2%;
}

/* Hover effect */
button:hover {
  background: linear-gradient(to bottom, #2980b9, #3498db);
  transform: translateY(-3px);
  box-shadow: 0px 6px 10px rgba(0, 0, 0, 0.2);
}


</style> -->
