export interface UserData {
    id: string;
    name: string;
    email: string;
}

export class User implements UserData {
    id: string;
    name: string;
    email: string;

    constructor(user: UserData) {
        this.id = user.id;
        this.name = user.name;
        this.email = user.email;
    }
}