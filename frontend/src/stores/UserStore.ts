import { defineStore } from "pinia";
import {computed, ref} from "vue";

// import type { User } from "@/domain/user.ts";
import AuthService from '@/services/AuthService.ts'
// import {decodeToken, removePrefixId} from "@/utils/utils.ts";
// import type {JwtPayload} from "@/domain/JwtPayload.ts";

export const useUserStore = defineStore(
    "user",
    () => {
        const user = ref();
        const session_token = ref()

        async function signUp(name: string, email: string, password: string) {
            try {
                const u = { name:name, email:email, password:password };
                const response = await AuthService.signUp(u);
                if(response.state === "VALIDATE_EMAIL") {
                    user.value = {
                        id: response.id,
                        name: name,
                        email: email,
                    }
                    return response.state;
                } else {
                    return response.state;
                }
            } catch (e) {
                console.error(e);
                throw e;
            }
        }

        async function signIn(email: string, password: string) {
            try {
                const response = await AuthService.signIn({email:email, password:password})
                if(response.status === 200) {
                    const token = response.data.session_token
                    const token_state = validateUserToken(token)
                    if (token_state === "USER_TOKEN_VALIDATED") {
                        return response.data.state;
                    }
                    return token_state
                } else {
                    return response.data.state;
                }
            } catch (e) {
                console.error(e);
                throw e;
            }
        }

        async function oauthSignIn(token: string) {
            try {
                const response = await AuthService.signIn({token: token})
                if(response.status === 200 || response.status === 201) {
                    const token = response.data.session_token
                    const token_state = validateUserToken(token)
                    if (token_state === "USER_TOKEN_VALIDATED") {
                        return response.data.state;
                    }
                    return token_state
                } else {
                    return response.data.state;
                }
            } catch (e) {
                console.error(e);
                throw e;
            }
        }

        function validateUserToken(token: any) {
            localStorage.setItem('jwt', token)
            const decoded: JwtPayload|null = decodeToken(token);
            if ( decoded && decoded.sub ) {
                user.value = {
                    id: decoded.sub.uid,
                    name: decoded.sub.name,
                    email: decoded.sub.email,
                    clubs: decoded.sub.clubs,
                    roles: decoded.sub.roles
                }
                session_token.value = token;
                return "USER_TOKEN_VALIDATED"
            }
            return "ERROR_VALIDATING_USER_TOKEN"
        }

        function signOut() {
            // Call BE to invalidate the token
            session_token.value = null;
            user.value = null;
        }

        async function resetPassword(password: string, token: string) {
            try {
                const response = await AuthService.resetPassword(password, token)
                if (response.status === 202) {
                    return response.data;
                } else {
                    return response.data;
                }
            } catch (e) {
                console.error(e);
                throw e;
            }
        }

        const isSessionTokenValid = computed(() => {
            if (session_token.value) {
                const decoded = decodeToken(session_token.value);
                if (decoded) {
                    const date = new Date().getTime()/1000;
                    return date>decoded.iat && date<decoded.exp
                }
                return false
            }
            return false;
        })
        return { user, session_token, signUp, signIn, oauthSignIn, signOut, isSessionTokenValid, resetPassword };
    },
    {
        persist: {
            key: "user",
            storage: sessionStorage
        },
    }
);
