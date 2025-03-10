<script setup lang="ts">
import { ref } from 'vue'

const contracts = ref([
  { id: 1, name: 'Contract A', status: 'Active' },
  { id: 2, name: 'Contract B', status: 'Pending' },
  { id: 3, name: 'Contract C', status: 'Expired' },
])
</script>

<template>
  <div class="contracts-page p-4">
    <h1 class="text-2xl font-bold mb-4">Contracts</h1>
    <table class="min-w-full bg-white">
      <thead>
        <tr>
          <th class="py-2 px-4 border-b">ID</th>
          <th class="py-2 px-4 border-b">Name</th>
          <th class="py-2 px-4 border-b">Status</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="contract in contracts" :key="contract.id">
          <td class="py-2 px-4 border-b">{{ contract.id }}</td>
          <td class="py-2 px-4 border-b">{{ contract.name }}</td>
          <td class="py-2 px-4 border-b">{{ contract.status }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template> 