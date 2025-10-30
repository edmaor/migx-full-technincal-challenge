<template>
  <Dialog v-model:visible="showEditDialog" header="Edit Participant" modal>
    <ParticipantForm mode="edit" :participant="editParticipant" @close="showEditDialog = false" />
  </Dialog>
  <DataTable v-model:filters="filters" :value="participantStore.participants" tableStyle="min-width: 50rem" removableSort
             :globalFilterFields="['study_group','status', 'gender', 'age']"
  >
    <template #header>
        <div class="flex justify-end">
            <IconField>
                <InputIcon>
                    <i class="pi pi-search" />
                </InputIcon>
                <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
            </IconField>
        </div>
    </template>
    <template #empty> No participants found. </template>
    <template #loading> Loading participants data. Please wait. </template>
    <Column field="participant_id" header="Participant"></Column>
    <Column field="subject_id" header="Subject" sortable></Column>
    <Column field="study_group" header="Study Group" sortable></Column>
    <Column field="enrollment_date" header="Enrollment Date" sortable></Column>
    <Column field="status" header="Status" sortable>
      <template #body="{ data }">
          <Tag :value="data.status" :severity="getSeverity(data.status)" />
      </template>
      <template #filter="{ filterModel, filterCallback }">
          <Select v-model="filterModel.value" @change="filterCallback()" :options="statuses" placeholder="Select One" style="min-width: 12rem" :showClear="true">
              <template #option="slotProps">
                  <Tag :value="slotProps.option" :severity="getSeverity(slotProps.option)" />
              </template>
          </Select>
      </template>
    </Column>
    <Column field="age" header="Age" sortable></Column>
    <Column field="gender" header="Gender" sortable></Column>
    <Column style="{width: 12rem}">
        <template #body="slotProps">
            <Button icon="pi pi-pencil" variant="outlined" rounded class="mr-2" @click="handleEditParticipant(slotProps.data)" />
            <Button icon="pi pi-trash" variant="outlined" rounded severity="danger" @click="handleDeleteParticipant(slotProps.data)" />
        </template>
    </Column>

  </DataTable>
</template>

<script setup lang="ts">
import {ref} from "vue";

import {useParticipantStore} from "@/stores/ParticipantStore.ts";

import { FilterMatchMode } from '@primevue/core/api';

import ParticipantForm from "@/partials/participant/PartcipantForm.vue";

import Dialog from 'primevue/dialog';
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';
import InputIcon from 'primevue/inputicon';
import InputText from 'primevue/inputtext';
import IconField from 'primevue/iconfield';
import Select from 'primevue/select';
import Tag from 'primevue/tag';
import Button from 'primevue/button';
import type {Participant} from "@/domain/Participant.ts";

const participantStore = useParticipantStore();
const filters = ref({
  global: { value: null, matchMode: FilterMatchMode.CONTAINS },
  study_group: { value: null, matchMode: FilterMatchMode.EQUALS },
  status: { value: null, matchMode: FilterMatchMode.EQUALS },
  age: { value: null, matchMode: FilterMatchMode.CONTAINS },
  gender: { value: null, matchMode: FilterMatchMode.EQUALS }
});

const statuses = ref(['active', 'completed', 'withdrawn'])
const getSeverity = (status: string) => {
  switch (status) {
    case 'withdrawn':
      return 'danger';

    case 'completed':
      return 'success';

    case 'active':
      return 'info';
    default:
      return 'warning';
  }
}

const showEditDialog = ref(false)
const editParticipant = ref<Participant>()

function handleEditParticipant(participant: Participant) {
  editParticipant.value = participant
  showEditDialog.value = true
}
</script>