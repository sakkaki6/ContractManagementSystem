<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()
</script>

<template>
  <div class="home">
    <header class="bg-primary-600 text-white p-4">
      <div class="container mx-auto">
        <h1 class="text-3xl font-bold">Contract Management System</h1>
      </div>
    </header>
    
    <main class="container mx-auto p-4">
      <div class="bg-white rounded-lg shadow-md p-6 mb-6">
        <h2 class="text-2xl font-semibold mb-4">Welcome to the Contract Management System</h2>
        <p class="mb-4">
          A comprehensive solution for managing contracts, approvals, and document workflows.
        </p>
        
        <div class="flex gap-4 mt-6">
          <button 
            class="bg-primary-600 hover:bg-primary-700 text-white px-4 py-2 rounded"
            @click="router.push('/login')"
          >
            Login
          </button>
        </div>
      </div>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div class="bg-white rounded-lg shadow-md p-6">
          <h3 class="text-xl font-semibold mb-3">Contract Management</h3>
          <p>Create, edit, and manage contracts with version control and full-text search.</p>
        </div>
        
        <div class="bg-white rounded-lg shadow-md p-6">
          <h3 class="text-xl font-semibold mb-3">Approval Workflows</h3>
          <p>Set up multi-step approval processes with notifications and e-signatures.</p>
        </div>
        
        <div class="bg-white rounded-lg shadow-md p-6">
          <h3 class="text-xl font-semibold mb-3">Analytics & Reporting</h3>
          <p>Track contract status, generate reports, and monitor compliance.</p>
        </div>
      </div>
    </main>
  </div>
</template> 