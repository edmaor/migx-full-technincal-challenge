<script setup lang="ts">
import { ref } from "vue";
import { Participant } from "@/domain/Participant";

interface FormState {
  id: string;
  participant_id: string;
  subject_id: string;
  study_group: string;
  enrollment_date: string;
  age: number | null;
  status: string;
  gender: string;
}

const props = defineProps<{
  mode: "create" | "edit"; // Determine form mode
  participant?: Participant; // Used to bind data in edit mode
}>();

// Reactive form state
const formState = ref<FormState>({
  id: "",
  participant_id: "",
  subject_id: "",
  study_group: "",
  enrollment_date: "",
  age: null,
  status: "",
  gender: "",
});

// Populate form state when in edit mode
if (props.mode === "edit" && props.participant) {
  Object.assign(formState.value, props.participant);
}

// Validation errors
const errors = ref<Record<string, string>>({});

// Simple form validation
const validateForm = (): boolean => {
  errors.value = {};

  if (!formState.value.participant_id) {
    errors.value.participant_id = "Participant ID is required.";
  }
  if (!formState.value.subject_id) {
    errors.value.subject_id = "Subject ID is required.";
  }
  if (!formState.value.study_group) {
    errors.value.study_group = "Study group is required.";
  }
  if (!formState.value.enrollment_date) {
    errors.value.enrollment_date = "Enrollment date is required.";
  }
  if (!formState.value.age || formState.value.age <= 0) {
    errors.value.age = "Age must be a positive number.";
  }
  if (!formState.value.status) {
    errors.value.status = "Status is required.";
  }
  if (!formState.value.gender) {
    errors.value.gender = "Gender is required.";
  }

  return Object.keys(errors.value).length === 0;
};

// Form submission handler
const handleSubmit = () => {
  if (validateForm()) {
    if (props.mode === "create") {
      console.log("Creating new participant:", formState.value);
      // Add API call or store logic here for creating a new participant
    } else if (props.mode === "edit") {
      console.log("Updating participant:", formState.value);
      // Add API call or store logic here for updating the participant
    }
  }
};
</script>

<template>
  <div class="participant-form space-y-4 min-w-[400px]">
    <form @submit.prevent="handleSubmit" class="space-y-4">
      <!-- Participant ID -->
      <div>
        <label for="participant_id" class="block mb-1 font-medium">Participant ID</label>
        <input
          id="participant_id"
          v-model="formState.participant_id"
          type="text"
          class="border rounded w-full p-2"
          :class="{ 'border-red-500': errors.participant_id }"
        />
        <p v-if="errors.participant_id" class="text-red-500 text-sm">
          {{ errors.participant_id }}
        </p>
      </div>

      <!-- Subject ID -->
      <div>
        <label for="subject_id" class="block mb-1 font-medium">Subject ID</label>
        <input
          id="subject_id"
          v-model="formState.subject_id"
          type="text"
          class="border rounded w-full p-2"
          :class="{ 'border-red-500': errors.subject_id }"
        />
        <p v-if="errors.subject_id" class="text-red-500 text-sm">
          {{ errors.subject_id }}
        </p>
      </div>

      <!-- Study Group -->
      <div>
        <label for="study_group" class="block mb-1 font-medium">Study Group</label>
        <input
          id="study_group"
          v-model="formState.study_group"
          type="text"
          class="border rounded w-full p-2"
          :class="{ 'border-red-500': errors.study_group }"
        />
        <p v-if="errors.study_group" class="text-red-500 text-sm">
          {{ errors.study_group }}
        </p>
      </div>

      <!-- Enrollment Date -->
      <div>
        <label for="enrollment_date" class="block mb-1 font-medium">Enrollment Date</label>
        <input
          id="enrollment_date"
          v-model="formState.enrollment_date"
          type="date"
          class="border rounded w-full p-2"
          :class="{ 'border-red-500': errors.enrollment_date }"
        />
        <p v-if="errors.enrollment_date" class="text-red-500 text-sm">
          {{ errors.enrollment_date }}
        </p>
      </div>

      <!-- Age -->
      <div>
        <label for="age" class="block mb-1 font-medium">Age</label>
        <input
          id="age"
          v-model.number="formState.age"
          type="number"
          class="border rounded w-full p-2"
          :class="{ 'border-red-500': errors.age }"
        />
        <p v-if="errors.age" class="text-red-500 text-sm">
          {{ errors.age }}
        </p>
      </div>

      <!-- Status -->
      <div>
        <label for="status" class="block mb-1 font-medium">Status</label>
        <select
          id="status"
          v-model="formState.status"
          class="border rounded w-full p-2"
          :class="{ 'border-red-500': errors.status }"
        >
          <option value="" disabled>Select status</option>
          <option value="active">Active</option>
          <option value="inactive">Inactive</option>
        </select>
        <p v-if="errors.status" class="text-red-500 text-sm">
          {{ errors.status }}
        </p>
      </div>

      <!-- Gender -->
      <div>
        <label for="gender" class="block mb-1 font-medium">Gender</label>
        <select
          id="gender"
          v-model="formState.gender"
          class="border rounded w-full p-2"
          :class="{ 'border-red-500': errors.gender }"
        >
          <option value="" disabled>Select gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
        <p v-if="errors.gender" class="text-red-500 text-sm">
          {{ errors.gender }}
        </p>
      </div>

      <button
        type="submit"
        class="btn w-full bg-blue-500 hover:bg-blue-600 text-white p-2 rounded"
      >
        {{ mode === "create" ? "Create" : "Update" }}
      </button>
    </form>
  </div>
</template>