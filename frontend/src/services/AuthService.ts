import http from "@/utils/http-common.ts";

class AuthService {
    async getUser(uid: string): Promise<any> {
        try {
            const response = await http.get(`/auth/user/${uid}`);
            console.log(response);
            return response.data;
        } catch (e) {
            console.error(e);
            throw e;
        }
    }

    async signUp(user: { name: string; email: string; password: string }) {
        try {
            const response = await http.post('/auth/users', JSON.stringify(user));
            return response.data;
        } catch (e) {
            console.error(e);
            throw e;
        }
    }

    async signIn(user: any) {
        try {
            return await http.post('/auth/sessions', JSON.stringify(user));
        } catch (e: any) {
            if (e.status === 401 && e.response.data.state === 'INVALID_CREDENTIALS') {
                return e.response;
            }
            console.error(e);
            throw e;
        }
    }

    async resetPassword(password: string, token: string) {
        try {
            return await http.put(`/auth/password`, JSON.stringify({ password: password, token: token}));
        } catch (e: any) {
            if (e.status === 404) {
                return e.response;
            }
            console.error(e);
            throw e;
        }
    }
}

export default new AuthService();