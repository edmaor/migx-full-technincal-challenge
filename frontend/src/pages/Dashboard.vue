<template>
  <main class="flex flex-col w-full gap-4">
    <nav class="flex gap-4 items-center justify-center w-full">
      <router-link to="/dashboard" exact-active-class="text-blue-500" class="text-lg font-bold">Metrics</router-link>
      <router-link to="/participants" exact-active-class="text-blue-500" class="text-lg font-bold">Participants</router-link>
    </nav>
    <div class="px-8">
      <router-view />
    </div>
  </main>
</template>

<script setup lang="ts">
import {onBeforeMount} from "vue";
import {useParticipantStore} from "@/stores/ParticipantStore.ts";

const participantStore = useParticipantStore();
onBeforeMount(async () => {
  await participantStore.getParticipants()
})
</script>