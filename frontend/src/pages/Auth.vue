<template>
  <main class="flex">
    <div class="flex-1 flex items-center justify-center flex-col w-full">
      <router-view />
    </div>
    <div class="flex-1 hidden lg:block">
      <img :src="authImage" alt="Scientist looking through a microscope">
    </div>
    
  </main>
</template>
<script setup lang="ts">
import authImage from "@/assets/auth.avif"
</script>