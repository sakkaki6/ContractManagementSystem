<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()

const email = ref('')
const password = ref('')
const errorMessage = ref('')

const login = async () => {
  if (!email.value || !password.value) {
    errorMessage.value = 'Please enter both email and password'
    return
  }

  try {
    const response = await axios.post('/api/auth/login', {
      email: email.value,
      password: password.value
    })

    // Assuming the response contains a token
    const token = response.data.token
    localStorage.setItem('authToken', token)

    // Redirect to home or dashboard
    router.push('/')
  } catch (error) {
    errorMessage.value = 'Login failed. Please check your credentials and try again.'
  }
}
</script>

<template>
  <div class="login-page min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
      <h1 class="text-2xl font-bold mb-6 text-center">Login to Contract Management System</h1>
      
      <div v-if="errorMessage" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
        {{ errorMessage }}
      </div>
      
      <form @submit.prevent="login" class="space-y-4">
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
          <input
            id="email"
            v-model="email"
            type="email"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
            placeholder="Enter your email"
          />
        </div>
        
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700 mb-1">Password</label>
          <input
            id="password"
            v-model="password"
            type="password"
            required
            class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
            placeholder="Enter your password"
          />
        </div>
        
        <div>
          <button
            type="submit"
            class="w-full bg-primary-600 hover:bg-primary-700 text-white py-2 px-4 rounded-md focus:outline-none focus:ring-2 focus:ring-primary-500"
          >
            Login
          </button>
        </div>
      </form>
      
      <div class="mt-4 text-center">
        <button
          class="text-primary-600 hover:text-primary-800"
          @click="router.push('/')"
        >
          Back to Home
        </button>
      </div>
    </div>
  </div>
</template> 