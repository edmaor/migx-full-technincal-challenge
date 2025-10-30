import { defineStore } from 'pinia'
import { ref } from 'vue'
import {Participant, type ParticipantData} from "@/domain/Participant.ts";
import ParticipantDataService from "@/services/ParticipantDataService.ts";

export const useParticipantStore = defineStore(
  'participants',
  () => {
      const participants = ref<Participant[]>([])

      async function addParticipant(participant: Participant) {}
      async function getParticipants() {
          const response = await ParticipantDataService.getParticipants()
          if (response) {
              participants.value = response;
          }
      }
      async function getParticipant(participant: string) {}
      async function updateParticipant(participant: Participant) {}
      async function removeParticipant(participant: string) {}
      return { participants, addParticipant, getParticipants, getParticipant, updateParticipant, removeParticipant }
  },
    {
        persist: {
            key: 'participants',
            storage: sessionStorage
        },
    }
)