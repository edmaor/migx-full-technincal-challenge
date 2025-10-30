export interface ParticipantData {
    id: string;
    participant_id: string;
    subject_id: string;
    study_group: string;
    enrollment_date: string;
    status: string;
    gender: string;
}

export class Participant implements ParticipantData {
    id: string;
    participant_id: string;
    subject_id: string;
    study_group: string;
    enrollment_date: string;
    status: string;
    gender: string;

    constructor(data: ParticipantData) {
        this.id = data.id;
        this.participant_id = data.participant_id;
        this.subject_id = data.subject_id;
        this.study_group = data.study_group;
        this.enrollment_date = data.enrollment_date;
        this.status = data.status;
        this.gender = data.gender;
    }
}