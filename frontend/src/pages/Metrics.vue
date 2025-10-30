<template>
  <main class="flex flex-col w-full gap-4">
    <h2 class="text-4xl font-bold">Metrics</h2>
    <div class="flex flex-col gap-4">
      <div class=""></div>
      {{ participantStore.participants.length }}
    </div>
  </main>
</template>

<script setup lang="ts">
import {useParticipantStore} from "@/stores/ParticipantStore.ts";

const participantStore = useParticipantStore();

</script>