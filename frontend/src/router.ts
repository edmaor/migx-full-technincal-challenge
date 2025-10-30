import { createRouter, createWebHistory } from "vue-router";

// AUTH && Children
import Auth from "@/pages/Auth.vue";
import Signin from "@/partials/auth/Signin.vue";
import Signup from "@/partials/auth/Signup.vue";
import ResetPassword from "@/partials/auth/ResetPassword.vue";

// DASHBOARD && Metrics
import Dashboard from "@/pages/Dashboard.vue";
import Metrics from "@/pages/Metrics.vue";

// ENTITIES
import Participants from "@/pages/Participants.vue";
// import {useUserStore} from "@/stores/UserStore.ts";

const routerHistory = createWebHistory();

const router = createRouter({
	history: routerHistory,
	routes: [
		{
			path: "/",
			component: Auth,
			children: [
				{
					path: "/",
					component: Signin,
				},
				{
					path: "/signup",
					component: Signup,
				},
				{
					path: "/reset-password",
					component: ResetPassword,
				},
			]
		},
        {
            path: "/dashboard",
            component: Dashboard,
            meta: {
                requiresAuth: true,
            },
            children: [
                {
                    path: "/dashboard",
                    component: Metrics,
                    meta: {
                        name: "Dashboard",
                    }
                },
                {
                    path: "/participants",
                    component: Participants,
                    meta: {
                        name: "Participants",
                    }
                }
            ]
        }
	],
});

router.beforeEach((to, from, next) => {
	// const userStore = useUserStore();

	// if (to.matched.some((record) => record.meta.requiresAuth)) {
    //     // if (userStore.user.role) {}
	// 	if (userStore.isSessionTokenValid) {
	// 		next();
	// 	} else {
	// 		next({ path: "/signin", query: { redirect: to.fullPath } });
	// 	}
	// } else {
	// 	next();
	// }
    console.log("beforeEach", to, from, next)
    next()
});

export default router;
