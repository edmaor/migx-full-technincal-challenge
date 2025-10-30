// import type { AxiosInstance, AxiosRequestConfig } from "axios";
import axios, { type AxiosInstance } from "axios";

const client: AxiosInstance = axios.create({
	baseURL: import.meta.env.VITE_API_URL,
	headers: {
		"Content-type": "application/json",
	},
});

client.interceptors.request.use(
	(config: any) => {
		const token = localStorage.getItem("session_token");
		if (token) {
			config.headers = {
				...config.headers,
				Authorization: `Bearer ${token}`,
			};
		}
		return config;
	},
	(error: any) => {
        console.error(error);
		return Promise.reject("No jwt detected");
	}
);

export default client;
