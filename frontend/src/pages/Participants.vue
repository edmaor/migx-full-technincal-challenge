<template>
  <main class="flex flex-col w-full gap-4">
    <div class="flex flex-row justify-between">
      <h2 class="text-4xl font-bold">Participants</h2>
      <span class="text-4xl font-bold text-blue-600" @click="showCreateParticipantDialog = true">+</span>
    </div>
    <Dialog v-model:visible="showCreateParticipantDialog" header="Create Participant" modal >
      <ParticipantForm mode="create" />
    </Dialog>
    <ParticipantTable />
  </main>
</template>

<script setup lang="ts">
import {ref} from "vue";

import ParticipantTable from "@/partials/participant/ParticipantTable.vue";
import ParticipantForm from "@/partials/participant/PartcipantForm.vue";
import Dialog from 'primevue/dialog';

const showCreateParticipantDialog = ref(false)
</script>