<template>
  <div class="login-container">
    <h2>系统登录</h2>
    <form @submit.prevent="handleLogin">
      <div class="input-group">
        <label for="username">用户名</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div class="input-group">
        <label for="password">密码</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">登录</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');
const router = useRouter();

const handleLogin = () => {
  // 假设正确的用户名是 'admin'，密码是 'password123'
  if (username.value === 'admin' && password.value === 'password123') {
    // 如果用户名和密码正确，跳转到欢迎页面
    router.push('/welcome');
  } else {
    // 如果用户名或密码错误，显示错误消息
    alert('用户名或密码错误');
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #2c3e50;
  color: white;
  padding: 2rem;
}

.input-group {
  margin-bottom: 1rem;
  width: 100%;
  max-width: 300px;
}

input[type="text"],
input[type="password"] {
  padding: 0.5rem;
  border: none;
  border-radius: 0.25rem;
  width: 100%;
  box-sizing: border-box;
}

button {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.25rem;
  background-color: #3498db;
  color: white;
  cursor: pointer;
  width: 100%;
  max-width: 300px;
}

button:hover {
  background-color: #2980b9;
}

h2 {
  text-align: center;
  margin-bottom: 2rem;
}
</style>