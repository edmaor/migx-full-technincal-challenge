import http from "@/utils/http-common.ts";
import {Participant, type ParticipantData} from "@/domain/Participant.ts";

class ParticipantDataService {
    async createParticipant(participant: ParticipantData) {
        try {
            const response = await http.post("/participants", participant)
            if (response.status === 201) {
                return response.data;
            } else {
                return null;
            }
        } catch (error) {
            console.error(error);
        }
    }

    async getParticipants() {
        try{
            const response = await http.get("/participants")
            if (response.status === 200 && Array.isArray(response.data)) {
                return response.data.map((item: any) => new Participant(item))
            } else return []
        } catch (error) {
            console.error(error);
        }
    }

    async getParticipant(id: string) {
        try{
            const response = await http.get(`/participant/${id}`)
            if (response.status == 200 && response.data) {
                return new Participant(response.data)
            } else {
                return null;
            }
        } catch (error) {
            console.error(error);
        }
    }

    async patchParticipant(id: string, participant: Partial<ParticipantData>) {
        try{
            const response = await http.patch(`/participant/${id}`, participant)
            if (response.status == 200 && response.data) {
                return new Participant(response.data)
            } else {
                return null;
            }
        } catch (error) {
            console.error(error);
        }
    }

    async deleteParticipant(id: string) {
        try{
            const response = await http.delete(`/participant/${id}`)
            return response.status == 200;
        } catch (error) {
            console.error(error);
        }
    }
}

export default new ParticipantDataService();