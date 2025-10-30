<template>
  <DataTable :value="participantStore.participants" tableStyle="min-width: 50rem">
    <Column field="participant_id" header="Participant"></Column>
    <Column field="subject_id" header="Subject"></Column>
    <Column field="study_group" header="Study Group"></Column>
    <Column field="enrollment_date" header="Enrollment Date"></Column>
    <Column field="status" header="Status"></Column>
    <Column field="age" header="Age"></Column>
    <Column field="gender" header="Gender"></Column>
  </DataTable>
</template>

<script setup lang="ts">
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import {useParticipantStore} from "@/stores/ParticipantStore.ts";

const participantStore = useParticipantStore();

</script>