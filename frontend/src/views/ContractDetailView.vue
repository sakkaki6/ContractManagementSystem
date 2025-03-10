<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const contractId = ref(route.params.id)

// Placeholder for contract details
const contractDetails = ref({
  id: contractId.value,
  name: `Contract ${contractId.value}`,
  status: 'Active',
  description: 'Detailed description of the contract goes here.'
})
</script>

<template>
  <div class="contract-detail-page p-4">
    <h1 class="text-2xl font-bold mb-4">Contract Details</h1>
    <div class="bg-white rounded-lg shadow-md p-6">
      <h2 class="text-xl font-semibold mb-2">{{ contractDetails.name }}</h2>
      <p class="mb-2"><strong>Status:</strong> {{ contractDetails.status }}</p>
      <p><strong>Description:</strong> {{ contractDetails.description }}</p>
    </div>
  </div>
</template> 