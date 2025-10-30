import { defineStore } from 'pinia'
import { ref } from 'vue'
import {Participant, type ParticipantData} from "@/domain/Participant.ts";
import ParticipantDataService from "@/services/ParticipantDataService.ts";

export const useParticipantStore = defineStore(
  'participants',
  () => {
      const participants = ref<Participant[]>([])

      async function addParticipant(participant: Participant) {
          const response = await ParticipantDataService.createParticipant(participant)
          if (response) {
              participants.value.push(response);
          }
      }

      async function getParticipants() {
          const response = await ParticipantDataService.getParticipants()
          if (response) {
              participants.value = response;
          }
      }

      async function getParticipant(participant: string) {
          const response = await ParticipantDataService.getParticipant(participant)
          if (response) {
              return response;
          }
          return null;
      }

      async function updateParticipant(participant: string, data: Partial<ParticipantData>) {
          const response = await ParticipantDataService.patchParticipant(participant, data)
          if (response) {
              return response;
          }
          return null;
      }

      async function removeParticipant(participant: string) {
          if ( await ParticipantDataService.deleteParticipant(participant)) {
              participants.value = participants.value.filter(p => p.id !== participant)
          }
          return participants.value;
      }

      return { participants, addParticipant, getParticipants, getParticipant, updateParticipant, removeParticipant }
  },
    {
        persist: {
            key: 'participants',
            storage: sessionStorage
        },
    }
)